from django import forms
from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    """
    The default

    """

    fullname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "input-form",
                "placeholder": "Fullname",
                "autocomplete": False,
            }
        ),
        label="Fullname",
        required=True,
    )
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "input-form",
                "placeholder": "Email",
                "autocomplete": False,
            }
        ),
        label="Email",
        required=True,
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "input-form",
                "placeholder": "Username",
                "autocomplete": False,
            }
        ),
        label="Username",
        required=True,
    )

    password1 = forms.CharField(
        max_length=30,
        min_length=6,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input-form",
                "autocomplete": False,
            }
        ),
    )
    password2 = forms.CharField(
        max_length=30,
        min_length=6,
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Comfirm Password",
                "class": "input-form",
                "autocomplete": False,
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "username", "fullname", "password1", "password2"]


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={"type": "email", "class": "input-form", "placeholder": "Email"}
        ),
        label="Email",
        required=True,
    )
    password = forms.CharField(
        max_length=30,
        min_length=6,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input-form",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            if not authenticate(
                email=self.cleaned_data["email"], password=self.cleaned_data["password"]
            ):
                raise forms.ValidationError("Invalid Username and Password")
