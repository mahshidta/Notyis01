from django import forms
from django.contrib.auth import authenticate

from accounts.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'input100',
            'placeholder': 'Email',
            'required': True
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'Password',
            'required': True
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(
                self.request,
                username=email,
                password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password.")
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100',
        'placeholder': 'Password',
        'required': True
    }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100',
        'placeholder': 'Confirm Password',
        'required': True
    }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input100',
                'placeholder': 'First Name',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input100',
                'placeholder': 'Last Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input100',
                'placeholder': 'Email',
                'required': True
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data