from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

# Create your views here.

# ----------------------------------  Employee details ------------------------------

def home(request):
	job_list = AddJobPost.objects.all()
	return render(request, 'employee/index.html', {'job_list': job_list})

def home_one(request, slug):
	job_one = AddJobPost.objects.get(slug=slug)
	return render(request, 'employee/home_one.html', {'job_one': job_one})

def employee_form(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			print "IF Valid @!!!"
			content = form.save(commit=False)
			content.user = request.user
			content.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/home')
		else:
			print form.errors
	form = EmployeeForm()
	return render(request, 'employee/employee_form.html', {'employee_form': form})

def search_jobs(request):
	filter_form = JobFilterForm()
	filter_form.fields["location__id"].queryset = Location.objects.all()
	filter_form.fields["add_job_types__id"].queryset = AddJobTypes.objects.all()
	filter_form.fields["add_job_category__id"].queryset = AddJobCategory.objects.all()
	if request.GET:
		tasks = AddJobPost(request.GET, queryset=tasks)
		filter_form = JobFilterForm(request.GET)
		if not request.GET['location__id'] == "":
			filter_form.fields['add_job_types__id'].queryset = AddJobTypes.objects.filter(location__id=request.GET['location__id'])
			filter_form.fields['add_job_category__id'].queryset = AddJobTypes.objects.filter(location__id=request.GET['location__id'])

		elif not request.GET['add_job_types__id'] == "":
			filter_form.fields['add_job_category__id'].queryset = AddJobTypes.objects.filter(add_job_types__id=request.GET['add_job_types__id'])	
		# return HttpResponseRedirect('')
	return render(request, 'employee/search_jobs.html', {'tasks': tasks, 'filter_form': filter_form})

# ---------------------------------- End Employee details ------------------------------

# ---------------------------------- Profile details ------------------------------

def profile(request):
	user = User.objects.get(username=request.user.username)

	# head_email = HeadEmail.objects.all()[0]
	# add_emails = AddEmail.objects.filter(head_email=head_email)

	add_emails = AddEmail.objects.all()

	# head_number = HeadNumber.objects.all()[0]
	# add_numbers = AddNumber.objects.filter(head_number=head_number)

	add_numbers = AddNumber.objects.all()

	# head_organization = HeadOrganization.objects.all()[0]
	# add_organization = AddOrganization.objects.filter(head_organization=head_organization)

	add_organization = AddOrganization.objects.all()

	# head_application = HeadApplication.objects.all()[0]
	# add_application = ClientApplication.objects.filter(head_application=head_application)

	add_application = ClientApplication.objects.all()

	variables = {'add_emails': add_emails, 'add_numbers': add_numbers,'add_organization': add_organization, 'add_application': add_application, 'user': user}
	return render(request, 'profile/profile.html', variables)

def edit_profile(request):
	edit_profile = User.objects.get(username=request.user.username)
	if request.method == "POST":
		form = SignupEditForm(request.POST, instance=edit_profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile')
		else:
			form.errors
	else:
		form = SignupEditForm(instance=edit_profile)
	return render(request, 'profile/edit_profile.html', {'sign_edit_form': form})

def change_password(request):
	account = User.objects.get(username=request.user.username)
	username = account.username
	if request.method == "POST":
		password = request.POST['password']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		user = auth.authenticate(username=username, password=password)
		if user:
			if password1 == password2:
				new_password = password1
			else:
				print "Password is Incorrect.."
			account.set_password(new_password)
			account.save()
			return HttpResponseRedirect('/signin')
	return render(request, 'profile/change_password.html')

# @csrf_exempt
def add_email(request):
	if request.method == "POST":
		form = AddEmailForm(request.POST)
		if form.is_valid():
			print "IF Valid @!!!"
			form.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/profile')
		else:
			print form.errors
	form = AddEmailForm()
	return render(request, 'profile/add_email.html', {'form': form})

def add_number(request):
	if request.method == "POST":
		form = AddNumberForm(request.POST)
		if form.is_valid():
			print "IF Valid @!!!"
			form.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/profile')
		else:
			print form.errors
	form = AddNumberForm()
	return render(request, 'profile/add_number.html')

def client_application(request):
	if request.method == "POST":
		form = ClientApplicationForm(request.POST)
		if form.is_valid():
			print "IF Valid @!!!"
			form.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/profile')
		else:
			print form.errors
	form = ClientApplicationForm()
	return render(request, 'profile/client_application.html', {'client_form': form})

def add_organization(request):
	if request.method == "POST":
		form = AddOrganizationForm(request.POST)
		if form.is_valid():
			print "IF Valid @!!!"
			form.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/profile')
		else:
			print form.errors
	form = AddOrganizationForm()
	return render(request, 'profile/add_organization.html') 

# ---------------------------------- End Profile details ------------------------------

# ---------------------------------- Employer details ------------------------------

def add_job_post(request):
	if request.method == "POST":
		form = AddJobPostForm(request.POST, request.FILES)
		if form.is_valid():
			print "IF Valid @!!!"
			form.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/home')
		else:
			print form.errors
	form = AddJobPostForm()
	return render(request, 'employer/add_job_post.html', { 'add_post_form': form })

def review(request):
	return render(request, 'employer/review.html')

def edit_post(request, post_id=1):
	edit_post = AddJobPost.objects.get(id=post_id)
	if request.method == "POST":
		form = AddJobPostForm(request.POST, request.FILES, instance=edit_post)
		if form.is_valid():
			print "IF Valid @!!!"
			form.save()
			print "IF Saved !!!!!!!"
			return HttpResponseRedirect('/profile')
		else:
			print form.errors
	form = AddJobPostForm(instance=edit_post)
	return render(request, 'employer/edit_post.html', {'edit_post': form})

def confirm(request):
	return render(request, 'employer/confirm.html')

def application_list(request):
	application_list = Employee.objects.filter(user=request.user)
	return render(request, 'employer/application_list.html', {'application_list': application_list})

def application_one(request, slug):
	application_one = Employee.objects.get(slug=slug)
	return render(request, 'employer/application_one.html', {'application_one': application_one})

# ---------------------------------- End Employer details ------------------------------

# ---------------------------------- Auth details ------------------------------

@csrf_exempt
def signup(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home'))
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			pass_verify = form.save(commit=False)
			print "This is first"
			if pass_verify.is_employee and pass_verify.is_employer:
				pass_verify.is_employer = False
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			if password1 == password2:
				password = password1
			else:
				print "Password is Incorrect.."
			pass_verify.set_password(password)
			pass_verify.save()
			return HttpResponseRedirect('/signin')
		else:
			form.errors
	else:
		form = SignupForm()
	return render(request, 'auth/sign_up.html', {'signup_form': form})

@csrf_exempt
def signin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home'))
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user:
			auth.login(request, user)
			division = Signup.objects.get(username=username)
			if division.is_employee:
				return HttpResponseRedirect('/home')
			else:
				return HttpResponseRedirect('/add-job-post')
		else:
			return HttpResponseRedirect('/signin')
	return render(request, 'auth/sign_in.html')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/home')

# ---------------------------------- End Auth details ------------------------------