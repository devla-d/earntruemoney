from django.urls import path
from . import views



urlpatterns = [
    path('sign-up/',views.sign_up, name="sign_up"),
    path('sign-in/',views.sign_in, name="sign_in"),
    path('sign-out/',views.sign_out, name="sign_out"),
    path('activate/<uidb64>/<token>/', views.account_activate_view, name='activate'),
]