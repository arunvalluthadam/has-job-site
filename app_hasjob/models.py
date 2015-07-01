from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.template.defaultfilters import slugify

# Create your models here.
class Signup(User): # AbstractBaseUser
	# email = models.EmailField(verbose_name = ('Email'),max_length=254, unique=True)
	is_employer = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)

	# USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['email']

	def __str__(self):  
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = ("Signup")
		verbose_name_plural = ("Signup")

# ------------------------------------ Employee Details -------------------------------------

class Employee(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	#slug
	slug = models.SlugField(unique=True, blank=True, null=True)
	phone = models.CharField(max_length=200)
	job_application = models.TextField()

	def __str__(self):  
		return self.name

	class Meta:
		verbose_name = ("Employee")
		verbose_name_plural = ("Employees")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.email)
		super(Employee, self).save(*args, **kwargs)

# ------------------------------------ End Employee Details ----------------------------------

# ------------------------------------ Employer Details ----------------------------------

class Location(models.Model):
	location = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def __str__(self):  
		return self.location

	class Meta:
		verbose_name = ("Location")
		verbose_name_plural = ("Locations")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.location)
		super(Location, self).save(*args, **kwargs)


class AddJobTypes(models.Model):
	types = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Add Job Type")
		verbose_name_plural = ("Add Job Types")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.types)
		super(AddJobTypes, self).save(*args, **kwargs)


class AddJobCategory(models.Model):
	category = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def __str__(self):  
		return self.category

	class Meta:
		verbose_name = ("Add Job Category")
		verbose_name_plural = ("Add Job Categories")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.category)
		super(AddJobCategory, self).save(*args, **kwargs)


class AddJobPost(models.Model):
	headline = models.CharField(max_length=200)
	owner_name = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
	types = models.ForeignKey(AddJobTypes)
	category = models.ForeignKey(AddJobCategory)
	# location = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	candidate_submit = models.TextField(null=True, blank=True)
	company = models.CharField(max_length=200)
	# slug
	slug = models.SlugField(unique=True,null=True, blank=True)
	logo = models.ImageField(verbose_name=u'Image', upload_to="uploads/logo", null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	date = models.DateField(auto_now_add=True) # , blank=True

	def __str__(self):  
		return self.owner_name

	class Meta:
		verbose_name = ("Add Job Post")
		verbose_name_plural = ("Add Job Posts")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.company)
		super(AddJobPost, self).save(*args, **kwargs)

# ------------------------------------ End Employer Details ----------------------------------

# ------------------------------------ Profile Details ---------------------------------------

class AddMailTypes(models.Model):
	types = models.CharField(max_length=200)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Add Mail Type")
		verbose_name_plural = ("Add Mail Types")

# class HeadEmail(models.Model):
# 	head = models.CharField(max_length=200)

# 	def __str__(self):  
# 		return self.head

# 	class Meta:
# 		verbose_name = ("Head Email")
# 		verbose_name_plural = ("Head Emails")

class AddEmail(models.Model):
	# head_email = models.ForeignKey(HeadEmail, null=True, blank=True)
	email = models.EmailField()
	types = models.ForeignKey(AddMailTypes)

	def __str__(self):  
		return self.email

	class Meta:
		verbose_name = ("Add Email")
		verbose_name_plural = ("Add Emails")


class AddNumberTypes(models.Model):
	types = models.CharField(max_length=200)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Add Number Type")
		verbose_name_plural = ("Add Number Types")

# class HeadNumber(models.Model):
# 	head = models.CharField(max_length=200)

# 	def __str__(self):  
# 		return str(self.head)

# 	class Meta:
# 		verbose_name = ("Head Number")
# 		verbose_name_plural = ("Head Numbers")

class AddNumber(models.Model):
	# head_number = models.ForeignKey(HeadNumber)
	number = models.IntegerField()
	types = models.ForeignKey(AddMailTypes)

	def __str__(self):  
		return str(self.number)

	class Meta:
		verbose_name = ("Add Number")
		verbose_name_plural = ("Add Numbers")


# class HeadOrganization(models.Model):
# 	head = models.CharField(max_length=200)

# 	def __str__(self):  
# 		return self.head

# 	class Meta:
# 		verbose_name = ("Head Organization")
# 		verbose_name_plural = ("Head Organizations")

class AddOrganization(models.Model):
	# head_organization = models.ForeignKey(HeadOrganization)
	organization_name = models.CharField(max_length=200)
	# slug
	slug = models.SlugField(unique=True, null=True, blank=True)
	username = models.CharField(max_length=200)
	domain = models.CharField(max_length=200)

	def __str__(self):  
		return self.organization_name

	class Meta:
		verbose_name = ("Add Organization")
		verbose_name_plural = ("Add Organizations")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.organization_name)
		super(AddOrganization, self).save(*args, **kwargs)



class ClientTypes(models.Model):
	types = models.CharField(max_length=200)

	def __str__(self):  
		return self.types

	class Meta:
		verbose_name = ("Client Type")
		verbose_name_plural = ("Client Types")

# class HeadApplication(models.Model):
# 	head = models.CharField(max_length=200)

# 	def __str__(self):  
# 		return self.head

# 	class Meta:
# 		verbose_name = ("HeadApplication")
# 		verbose_name_plural = ("HeadApplications")

class ClientApplication(models.Model):
	# head_application = models.ForeignKey(HeadApplication, null=True, blank=True)
	application_title = models.CharField(max_length=200)
	# slug
	slug = models.SlugField(unique=True, null=True, blank=True)
	description = models.TextField()
	types = models.ForeignKey(ClientTypes)
	application_website = models.URLField()
	redirect_url = models.URLField()
	notification_url = models.URLField()

	def __str__(self):  
		return self.application_title

	class Meta:
		verbose_name = ("Client Application")
		verbose_name_plural = ("Client Applications")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.application_title)
		super(ClientApplication, self).save(*args, **kwargs)


# ------------------------------------ End Profile Details ----------------------------------
