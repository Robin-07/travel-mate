from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=24,required=False,label="First Name",widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=24,required=False,label="Last Name",widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def clean(self):
        super(CustomSignupForm, self).clean()
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if last_name and not first_name:
            self.add_error('last_name', "Must add first name with last name.")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user