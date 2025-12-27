from django import forms
from django.contrib.auth.models import User

class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ['username', 'email', 'password']



    # email = forms.EmailField(widget=forms.EmailField(attrs={'class'='input100'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class'='input100'}))



# class EmailRegisterForm(forms.Form):
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={
#             "class": "input100",
#             "placeholder": "Email"
#         })
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             "class": "input100",
#             "placeholder": "Password"
#         })
#     )







