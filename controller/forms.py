from django import forms
from .models import Member, Address

SEX_CHOICES = (
    ("M", "MALE"),
    ("F", "FEMALE")
)

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