from django import forms
from accounts.models import Account


from .models import Packages


GENDER  = (
		('MALE', "Male"),
		('FEMALE', "Female"),
	)


class UserUpdateForm(forms.ModelForm):

    country = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'input-form',
                "placeholder":'Country'
            }
        ),
        label = 'Country',
        required=True
    )
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'input-form',
                "placeholder":'City'
            }
        ),
        label = 'City',
        required=True
    )
    # state = forms.CharField(
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             'type': 'text',
    #             'class': 'input-form',
    #             "placeholder":'State'
    #         }
    #     ),
    #     label = 'State',
    #     required=True
    # )
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'input-form',
                "placeholder":'ADDRESS'
            }
        ),
        label = 'Address',
        required=True
    )
 
    zipcode = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'input-form',
                "placeholder":'zipcode'
            }
        ),
        label = 'Zipcode',
        required=True
    )
    gender = forms.CharField(
            widget=forms.Select(
                choices = GENDER,
                attrs={
                    'class': 'browser-default custom-select',
                     'class': 'input-form',
                }
            ),
            label = "Gender",
            required=True
    )
    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'tel',
                'class': 'input-form',
                "placeholder":'Phone Number'
            }
        ),
        label = 'Phone Number',
        required=True
    )

 

    date_of_birth = forms.CharField( 
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'input-form'
            }
        ),
        label = 'Date Of Birth',
        required=True
    )


    class Meta:
        model = Account
        fields = ['country','city','address','zipcode','gender','phone','date_of_birth']







class PasswordChangeForm(forms.ModelForm):
    user_id = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'hidden',
                'class': 'input-form',

            }
        ),
        label = "",
        required=True
    )
    oldpassword = forms.CharField( max_length=30, label='Old password', widget=forms.PasswordInput(attrs={'placeholder': "OLD PASSWORD", 'class': 'input-form',}))
    password1 = forms.CharField( max_length=30, label='New Password', widget=forms.PasswordInput(attrs={'placeholder': "NEW PASSWORD", 'class': 'input-form',}))
    password2 = forms.CharField( max_length=30, label='Comfirm Password', widget=forms.PasswordInput(attrs={'placeholder': "CONFIRM NEW PASSWORD", 'class': 'input-form',}))

    class Meta:
        model = Account
        fields = ['user_id','oldpassword','password1','password2']

    def clean(self):
        if self.is_valid():
            user_id = self.cleaned_data['user_id']
            oldpassword = self.cleaned_data['oldpassword']
            password1 =  self.cleaned_data['password1']
            password2 =  self.cleaned_data['password2']
            user = Account.objects.get(id=user_id)
            if password1 != password2:
                raise forms.ValidationError("Passwords don\'t match")
            if not user.check_password(oldpassword):
                raise forms.ValidationError("Old password don\'t match")











class NewPackageForm(forms.ModelForm):

    class Meta:
        model = Packages
        fields = ('name','hours','percent','ref_percent','min_amount','max_amount')