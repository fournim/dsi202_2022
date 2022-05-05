from django import forms
from myapp.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','address','postcode','phone','email']