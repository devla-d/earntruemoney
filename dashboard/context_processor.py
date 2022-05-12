#from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from dashboard.models import Notification




def dashboard_processor(request):
    current_site = get_current_site(request)
    context = {}
    context['domain']  = current_site.domain
    if request.user.is_authenticated:
        context['referral_bonus']  =      request.user.referral_bonus
        context['referral']        =      request.user.referral
        context['unique_id']       =      request.user.unique_id
        context['notifications']    =      Notification.objects.filter(user=request.user)

        return context
    context['err']           =      "Please Login"
    return context
    