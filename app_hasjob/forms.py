from django import forms
from django.forms.models import inlineformset_factory
from .models import *

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ('first_name', 'last_name', 'username', 'email', 'is_employer', 'is_employee')
		widgets = {
			'first_name': forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Enter First Name"}),
			'last_name': forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Enter Last Name"}),
			'username': forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Enter Username"}),
			'email': forms.TextInput(attrs={"class":"form-control", "type":"email", "placeholder":"Enter Your Email"}),
			'is_employer': forms.CheckboxInput(),
			'is_employee': forms.CheckboxInput(),
		}

# -------------------------------------- profile details ----------------------------------------

class SignupEditForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ('first_name', 'last_name', 'username', 'email', 'is_employer', 'is_employee')
		widgets = {
			'first_name': forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Enter First Name"}),
			'last_name': forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Enter Last Name"}),
			'username': forms.TextInput(attrs={"class":"form-control", "type":"text", "placeholder":"Enter Username"}),
		}

class AddEmailForm(forms.ModelForm):
	class Meta:
		model = AddEmail
		fields = ('email', 'types')
		exclude = ('head_email',)
		widgets = {
			'email': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Email"}),
			'types': forms.Select(attrs={"class": "radio"}),
		}
# AddEmailFormSet = inlineformset_factory(HeadEmail, AddEmail, form=AddEmailForm, can_delete=False, extra=1)


class AddNumberForm(forms.ModelForm):
	class Meta:
		model = AddNumber
		exclude = ('head_number',)
		widgets = {
			'number': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Number"}),
			'types': forms.RadioSelect(attrs={"class": "radio"}),
		}
# AddNumberFormSet = inlineformset_factory(HeadNumber, AddNumber, form=AddNumberForm, can_delete=False, extra=1)


class AddOrganizationForm(forms.ModelForm):
	class Meta:
		model = AddOrganization
		exclude = ('head_organization',)
		widgets = {
			'organization_name': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Email"}),
			'username': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Email"}),
			'domain': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Email"}),
		}
# AddNumberFormSet = inlineformset_factory(HeadOrganization, AddOrganization, form=AddOrganizationForm, can_delete=False, extra=1)


class ClientApplicationForm(forms.ModelForm):
	class Meta:
		model = ClientApplication
		exclude = ('head_application',)
		widgets = {
			'application_title': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Application Title"}),
			'description': forms.Textarea(attrs={"class": "form-control", "type": "text", "placeholder": "Description"}),
			'types': forms.RadioSelect(attrs={"class": "radio"}),
			'application_website': forms.URLInput(attrs={"class": "form-control", "type": "text", "placeholder": "Application Website"}),
			'redirect_url': forms.URLInput(attrs={"class": "form-control", "type": "text", "placeholder": "Redirect URL"}),
			'notification_url': forms.URLInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Notification URL"}),
		}
# AddNumberFormSet = inlineformset_factory(HeadApplication, ClientApplication, form=ClientApplicationForm, can_delete=False, extra=1)

# -------------------------------------- End profile details ------------------------------------

# -------------------------------------- Employer Details ------------------------------------

class AddJobPostForm(forms.ModelForm):
	class Meta:
		model = AddJobPost
		exclude = ('date', 'slug')
		widgets = {
			'headline': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Head Line"}),
			'owner_name': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Name of Employer"}),
			'types': forms.RadioSelect(attrs={"class": "radio"}),
			'category': forms.RadioSelect(attrs={"class": "radio"}),
			'location': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Location"}),
			'description': forms.Textarea(attrs={"class": "form-control", "type": "text", "placeholder": "Description", "rows": "5"}),
			'candidate_submit': forms.Textarea(attrs={"class": "form-control", "type": "text", "placeholder": "Candidate Submit", "rows": "5"}),
			'company': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "name"}),
			'logo': forms.FileInput(attrs={"class":"form-control"}),
			'url': forms.URLInput(attrs={"class": "form-control", "type": "text", "placeholder": "URL"}),
			'twitter': forms.URLInput(attrs={"class": "form-control", "type": "text", "placeholder": "Twitter"}),
			'email': forms.TextInput(attrs={"class": "form-control", "type": "email", "placeholder": "Enter Email"}),
		}

# -------------------------------------- End Employer Details ------------------------------------

# -------------------------------------- Employee Details ------------------------------------

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		exclude = ('user', 'date', 'slug')
		widgets = {
			'name': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Name"}),
			'email': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Enter Email"}),
			'phone': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Phone"}),
			'job_application': forms.Textarea(attrs={"class": "form-control", "type": "text", "placeholder": "Job Application"}),
		}

# -------------------------------------- End Employee Details ------------------------------------
