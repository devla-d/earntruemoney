"""earntruemoney URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("", include("accounts.urls")),
    path("superadmin/", include("superadmin.urls")),
    path(
        "password-reset/",
        auth_view.PasswordResetView.as_view(template_name="auth/password-reset.html"),
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="auth/password-reset-done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="auth/password-reset-confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_view.PasswordResetCompleteView.as_view(
            template_name="auth/password-reset-complete.html"
        ),
        name="password_reset_complete",
    ),
]


handler404 = "superadmin.views.page_not_found_view"
