from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.dashboard,name='admindashboard'),
    path('users/',views.users,name='users'),
    path('users/<int:pk>',views.user_detail,name='user_detail'),
    path('withdrawals/',views.withdrawal_,name='withdrawal_super'),
    path('withdrawals/<int:pk>',views.withdrawal_detail,name='withdrawal_detail'),

    path('deposits/',views.deposit_,name='deposit_'),

    path('users/<int:pk>/login/',views.login_user_account,name='login_user_account'),


    path('investments/',views.investments,name='investments'),
    path('investments/<int:pk>',views.investments_detail,name='investments_detail'),

    path('packages/',views.packages_,name='packages_'),
    
    ]
