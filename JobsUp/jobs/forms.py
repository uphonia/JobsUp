from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length = 200, required = True)
    last_name = forms.CharField(max_length = 200, required = True)
    email = forms.CharField(max_length = 200, required = True)
    password = forms.CharField(max_length = 200, required = True)
    company_name = forms.CharField(max_length = 200, required = False)
    area_of_interest = forms.CharField(max_Length = 200, required = False)
    jobs = forms.CharField(max_Length = 500, required = False)

class LogIn(forms.Form):
	email = forms.CharField(max_length = 200, required = True)
    password = forms.CharField(max_length = 200, required = True)