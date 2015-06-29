from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Signup)
admin.site.register(AddMailTypes)
admin.site.register(AddNumberTypes)
admin.site.register(ClientTypes)

# ------------------------------------ Profile Details ---------------------------------------

class AddEmailAdmin(admin.ModelAdmin):
	model = AddEmail
	list_display = ['email', 'types']

admin.site.register(AddEmail, AddEmailAdmin)

# class AddEmailInline(admin.StackedInline):
# 	model = AddEmail
# 	extra = 1


# class HeadEmailAdmin(admin.ModelAdmin):
# 	model = HeadEmail
# 	list_display = ['head']
# 	inlines = [AddEmailInline]

# admin.site.register(HeadEmail, HeadEmailAdmin)

class AddNumberAdmin(admin.ModelAdmin):
	model = AddNumber
	list_display = ['number', 'types']

admin.site.register(AddNumber, AddNumberAdmin)

# class AddNumberInline(admin.StackedInline):
# 	model = AddNumber
# 	extra = 1


# class HeadNumberAdmin(admin.ModelAdmin):
# 	model = HeadNumber
# 	list_display = ['head']
# 	inlines = [AddNumberInline]

# admin.site.register(HeadNumber, HeadNumberAdmin)

class AddOrganizationAdmin(admin.ModelAdmin):
	model = AddOrganization
	list_display = ['organization_name', 'username', 'domain']

admin.site.register(AddOrganization, AddOrganizationAdmin)

# class AddOrganizationInline(admin.StackedInline):
# 	model = AddOrganization
# 	extra = 1

# class HeadOrganizationAdmin(admin.ModelAdmin):
# 	model = HeadOrganization
# 	list_display = ['head']
# 	inlines = [AddOrganizationInline]

# admin.site.register(HeadOrganization, HeadOrganizationAdmin)

class ClientApplicationAdmin(admin.ModelAdmin):
	model = ClientApplication
	list_display = ['application_title', 'description', 'types', 'application_website', 'redirect_url', 'notification_url']

admin.site.register(ClientApplication, ClientApplicationAdmin)

# class ClientApplicationInline(admin.StackedInline):
# 	model = ClientApplication
# 	extra = 1

# class HeadApplicationAdmin(admin.ModelAdmin):
# 	model = HeadApplication
# 	list_display = ['head']
# 	inlines = [ClientApplicationInline]

# admin.site.register(HeadApplication, HeadApplicationAdmin)

# ------------------------------------ End Profile Details ----------------------------------

# ------------------------------------ Employer Details ----------------------------------

admin.site.register(AddJobTypes)
admin.site.register(AddJobCategory)

class AddJobPostAdmin(admin.ModelAdmin):
	model = AddJobPost
	list_display = ['headline', 'types', 'category', 'location', 'description', 'candidate_submit', 'company', 'slug', 'logo', 'url', 'twitter', 'email', 'date']

admin.site.register(AddJobPost, AddJobPostAdmin)

# ------------------------------------ End Employer Details ----------------------------------

# ------------------------------------ Employee Details ----------------------------------

class EmployeeAdmin(admin.ModelAdmin):
	model = Employee
	list_display = ['user', 'name', 'email', 'phone', 'job_application']

admin.site.register(Employee, EmployeeAdmin)

# ------------------------------------ End Employee Details ----------------------------------