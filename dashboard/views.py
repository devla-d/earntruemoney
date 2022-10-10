from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from earntruemoney import utils
from django.contrib import messages
from accounts.models import Account, LoginHistory, Referral
from .models import *
from .forms import UserUpdateForm, PasswordChangeForm


@login_required
def index(request):
    user = request.user
    try:
        investment = Investments.objects.get(user=user)
    except Investments.DoesNotExist:
        investment = None
    earnings = 0
    if user.referral_bonus == user.balance:
        earnings = user.balance
    else:
        earnings = user.balance - user.referral_bonus
    context = {
        "logs": LoginHistory.objects.filter(user=user).order_by("-date")[:3],
        "investment": investment,
        "earnings": earnings,
    }
    return render(request, "users/index.html", context)


@login_required
def withdrawal_(request):
    user = request.user
    if request.POST:
        accountnum = request.POST.get("accountnum")
        accountname = request.POST.get("accountname")
        bank = request.POST.get("bank")
        amount = int(request.POST.get("amount"))

        if user.balance >= amount:
            bank = Bank.objects.create(
                acc_name=accountname, acc_num=accountnum, ty_pe=bank
            )
            transaction = Transactions.objects.create(
                user=user,
                amount=amount,
                trans_type=utils.W,
                unique_u=utils.trans_code(),
            )
            transaction.bank_details = bank
            user.balance -= amount
            user.save()
            transaction.save()
            messages.success(request, ("Withdrawal Placed !"))
            return redirect("withdrawal_")
        else:
            messages.warning(request, ("Insufficient Funds!"))
            return redirect("withdrawal_")

    return render(request, "users/withdrawal.html")


@login_required
def transactions_(request):
    transactions = Transactions.objects.filter(user=request.user).order_by("-date")
    return render(request, "users/transaction.html", {"transactions": transactions})


@login_required
def settings_(request):
    user = request.user
    if request.POST:
        submit = request.POST.get("submit")
        if submit == "UpdateProfile":
            u_form = UserUpdateForm(request.POST, instance=user)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, ("Account Updated !"))
                return redirect("settings_")
        # elif submit == "ChangePassword":
        #     p_form = PasswordChangeForm(request.POST,instance=user)
        #     if p_form.is_valid():
        #         password1 = p_form.cleaned_data['password1']
        #         user.set_password(password1)
        #         user.save()
        #         messages.success(request, f'Password Change')
        #         return redirect('settings_')
        else:
            messages.warning(request, f"UNKNOWN ERROR OCCURED !")
            return redirect("settings_")

    else:
        u_form = UserUpdateForm(instance=user)
        # p_form = PasswordChangeForm(initial={'user_id': user.id})
    return render(request, "users/settings.html", {"u_form": u_form})


@login_required
def change_password_view(request):
    user = request.user
    if request.POST:
        p_form = PasswordChangeForm(request.POST, instance=user)
        if p_form.is_valid():
            password1 = p_form.cleaned_data["password1"]
            user.set_password(password1)
            user.save()
            messages.success(request, f"Password Change")
            return redirect("change_password")
        else:
            messages.warning(request, f"Passwords don't match")
            return redirect("change_password")
    else:
        p_form = PasswordChangeForm(initial={"user_id": user.id})
    return render(request, "users/changepassword.html", {"p_form": p_form})


@login_required
def create_investment(request):
    packages = Packages.objects.all()
    user = request.user
    investment, created = Investments.objects.get_or_create(user=user)
    if request.POST:
        package_id = int(request.POST.get("package"))
        amount = int(request.POST.get("amount"))
        package = get_object_or_404(Packages, pk=package_id)
        if user.deposit_balance >= amount:
            if amount not in range(package.min_amount, package.max_amount):
                messages.warning(
                    request, (f"Input Amount Between Your Selected Plans Price")
                )
                return redirect("create_investment")
            else:
                investment.end_date = utils.get_deadline(package.hours)
                investment.start_date = timezone.now()
                investment.status = "active"
                investment.amount_invested = amount
                investment.package = package
                user.deposit_balance -= amount
                # user.total_amount_invested +=  amount
                # user.total_investement_count += 1
                user.save()
                investment.save()
                messages.success(request, ("YOUR INVESTMENT HAS BEEN ACTIVATED"))
                return redirect("dashboard")
        else:
            messages.warning(request, ("INSUFFICIENT FUNDS,PLEASE DEPOSIT"))
            return redirect("create_investment")
    return render(request, "users/create_investment.html", {"packages": packages})


def end_user_investment_view(request):
    if request.POST:
        user = request.user
        investment = get_object_or_404(Investments, user=user)
        investment.status = "completed"
        investment.amount_earn += utils.earnings(
            investment.amount_invested, investment.package.percent
        )
        user.balance += utils.earnings(
            investment.amount_invested, investment.package.percent
        )
        user.save()
        investment.save()
        Notification.objects.create(
            user=user,
            title="Investment Has Been Completed",
            body=f" YOUR INVESTMENT OF ${investment.amount_invested} HAS BEEN COMPLETED YOU CAN NOW RENEW OR UPGRADE YOUR PLAN",
        )
        return JsonResponse({"msg": "Account Credited"})
    else:
        return JsonResponse({"msg": "Get Request Not Accepted"})


def homepage(request):
    return render(request, "homepage.html")


def aboutpage(request):
    return render(request, "aboutpage.html")


def partnerspage(request):
    return render(request, "partnerpage.html")


def faqpage(request):
    return render(request, "faqpage.html")


def privacypage(request):
    return render(request, "privacypage.html")


def contactpage(request):
    return render(request, "contactpage.html")
