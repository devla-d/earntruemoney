from venv import create
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta,datetime

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_str
from django.core.mail import EmailMessage
from django.template.loader import get_template


from earntruemoney import utils
from .forms import RegisterForm,LoginForm
from .models import Account,LoginHistory,Referral


def sign_up(request):
    if request.GET.get('ref-code'):
        ref_code =  request.GET.get('ref-code')
    else:
        ref_code = None
    if request.GET.get('act'):
        act =  request.GET.get('act')
    else:
        act = None
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = False
            instance.unique_id = utils.reg_code()
            instance.save()

            if ref_code != None:
                try:
                    old_user =  Account.objects.get(unique_id=ref_code)
                except Account.DoesNotExist:
                    messages.warning(request, ('UNKNOWN ERROR OCCURED !'))
                    return redirect(f'/sign-up/')
                old_user_ref_model = Referral.objects.get(user=old_user)
                new_user_ref_model,created  = Referral.objects.get_or_create(user=instance,referred_by=old_user)

                old_user.referral_bonus += 10
                old_user.balance        += 10
                old_user.referral       += 1
                old_user.save()

                old_user_ref_model.referrals.add(instance)

                new_user_ref_model.referred_by = old_user
            else:

                Referral.objects.create(user=instance)


            current_site = get_current_site(request)
            subject = 'Email Address Confirmation'
            context = {
                'user': instance,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
                'token': default_token_generator.make_token(instance),
                }
            message = get_template("auth/account_activation_email.html").render(context)
            mail = EmailMessage(
                subject=subject,
                body=message,
                from_email=utils.EMAIL_ADMIN,
                to=[instance.email],
                reply_to=[utils.EMAIL_ADMIN],
            )
            mail.content_subtype = "html"
            mail.send(fail_silently=True)





            return redirect(f'/sign-up/?act=verify-email')
    else:
        form = RegisterForm()
    return render(request,'auth/signup.html',{'ref_code':ref_code,"form":form,'act':act})







def account_activate_view(request, uidb64, token, *args, **kwargs):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_email_verifield = True
        user.save()
        login(request, user)
        messages.success(request, ('Please Complete Your Account Setup'))
        return redirect('dashboard')
    else:
        messages.warning(request, ('The confirmation link is invalid, possibly because it has already been used.'))
        return redirect('sign_up')







def sign_in(request):
    destination = utils.get_next_destination(request)
    print(destination)
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                LoginHistory.objects.create(user=user,log_ip=utils.get_client_ip(request),city='los vegas')
                if destination:
                    return redirect(f'{destination}') 
                else:
                    return redirect('dashboard')
                # return redirect('dashboard')
        else:
            messages.warning(request, ('Invalid Username Or Password.'))
            return redirect('sign_in')
    else:
        form   = LoginForm()
    return render(request,'auth/signin.html',{'form':form})


def sign_out(request):
    logout(request)
    return redirect('sign_in')