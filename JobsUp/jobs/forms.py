from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(max_length = 200, required = True)
	first_name = forms.CharField(max_length = 200, required = True)
	last_name = forms.CharField(max_length = 200, required = True)
	email = forms.EmailField(max_length = 254, required = True)
	password = forms.CharField(max_length = 200, required = True)
	personnel = forms.CharField(max_length = 200, required = True)

class LogInForm(forms.Form):
	username = forms.CharField(max_length = 200, required = True)
	password = forms.CharField(max_length = 200, required = True)

class ProfileForm(forms.Form):
	hashid = forms.CharField(max_length = 200, required = True)
	company_name = forms.CharField(max_length = 200, required = False)
	first_name = forms.CharField(max_length = 200, required = False)
	last_name = forms.CharField(max_length = 200, required = False)
	email = forms.EmailField(max_length = 200, required = True)
	phone_num = forms.CharField(max_length = 200, required = True)
	str_address = forms.CharField(max_length = 500, required = True)
	city = forms.CharField(max_length = 500, required = True)
	state = forms.CharField(max_length = 500, required = True)
	zipcode = forms.CharField(max_length = 500, required = True)
	website = forms.CharField(max_length = 200, required = False)
	degree = forms.CharField(max_length = 200, required = False)
	resume = forms.CharField(max_length = 200, required = False)

class MapRequestForm(forms.Form):
	hashid = forms.CharField(max_length = 200, required = True)
	radius = forms.CharField(max_length = 200, required = True)

class ViewApplicationForm(forms.Form):
	hashid = forms.CharField(max_length = 200, required = True)
