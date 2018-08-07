from django import forms
from .models import User


class SignupForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=50,required=True)
    lname = forms.CharField(label="Last Name", max_length=50,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(label="New Password", max_length=10, widget=forms.PasswordInput, required=True)
    repassword = forms.CharField(label="Re-type Password", max_length=10, widget=forms.PasswordInput, required=True)

    class Meta:
        model = User

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(user_email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')

    def clean_repassword(self):
        psw = self.cleaned_data.get('password')
        repsw = self.cleaned_data.get('repassword')
        if psw != repsw:
            raise forms.ValidationError("Password doesn't match!")
        return self.cleaned_data


class LoginForm(forms.Form):

    username = forms.CharField(label="Email/Username", max_length=50,required=True)
    password = forms.CharField(label="Password", max_length=10,widget=forms.PasswordInput,required=True)

    class Meta:
        model = User

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(user_email=username)
            if user.user_password != password:
                raise forms.ValidationError("Sorry, wrong username or password !")
        except User.DoesNotExist:
                raise forms.ValidationError("Invalid Login")
        return self.cleaned_data


