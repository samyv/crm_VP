from django import forms
from .models import Member, Address
from django.contrib.auth.forms import AuthenticationForm


SEX_CHOICES = (
    ("M", "MALE"),
    ("F", "FEMALE")
)


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'required class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
            'name': 'username',
            'type': 'username',
            'autocomplete': "username",
            'placeholder': 'put in your username..',
            'id': 'username'
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'required class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
            'name': 'password',
            'type': 'password',
            'autocomplete': "current-password",
            'placeholder': '***********',
            'id': 'password'
        }
))


class MemberModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'email', 'is_staff', 'sex', 'address')

class MemberForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    address = forms.ModelChoiceField(queryset=Address.objects.all())