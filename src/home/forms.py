from django import forms
from .helpers import past_years


class ProfileForm(forms.Form):

    photo = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=20,required=False,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=20,required=False,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    dob = forms.DateField(required=False,widget=forms.SelectDateWidget(years=past_years(100),attrs={'placeholder':'D.O.B'}))
    phone = forms.CharField(max_length=10,required=False,widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
