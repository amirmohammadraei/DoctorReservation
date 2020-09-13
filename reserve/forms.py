from django import forms
from .models import User, VisitTime


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }


class UserSignUp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'password')
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'username': 'Username',
            'phone_number': 'Phone number',
            'password': 'Password',
        }


class Verification(forms.ModelForm):
    class Meta:
        model = User
        fields = ('verify',)
        labels = {
            'verify': 'Verification Code',
        }


class FirstName(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',)
        labels = {
            'first_name': 'First Name',
        }


class LastName(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name',)
        labels = {
            'last_name': 'Last Name',
        }


class Password(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
        labels = {
            'password': 'Password',
        }


class Image(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image',)
        labels = {
            'image': 'Image',
        }


class Visit(forms.ModelForm):
    class Meta:
        model = VisitTime
        fields = ('date', 'start_time', 'end_time')
        labels = {
            'date': 'Date',
            'start_time': 'Start',
            'end_time': 'End',
        }


class VisitTimeChoice(forms.Form):
    id = forms.IntegerField()


class Username(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        labels = {
            'username': 'Username',
        }
