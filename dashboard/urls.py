from django.urls import path


from . import views


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('about/',views.aboutpage,name="aboutpage"),
    path('partners/',views.partnerspage,name="partnerspage"),
    path('faqs/',views.faqpage,name="faqpage"),
    path('privacy/',views.privacypage,name="privacypage"),
    path('support/',views.contactpage,name="contactpage"),


    path('index/',views.index,name='dashboard'),

    path('withdraw-funds/',views.withdrawal_,name='withdrawal_'),

    path('transactions/',views.transactions_,name='transactions_'),

    path('account-settings/',views.settings_,name='settings_'),

    path('change-password/',views.change_password_view,name='change_password'),
    path('create-investment/',views.create_investment,name='create_investment'),


     path('credit-user-investment/', views.end_user_investment_view, name="end_user_investment_view"),


]