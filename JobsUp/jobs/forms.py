from django import forms

class UserForm(form.form):
    first_name = forms.CharField(max_length = 200, required = False)
    last_name = forms.CharField(max_length = 200, required = False)
    email = forms.CharField(max_length = 200, required = False)
    password = forms.CharField(max_length = 200, required = False)