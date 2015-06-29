from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:

# ----------------------------- Employee Details -----------------------------------------

    url(r'^home/$', 'app_hasjob.views.home', name='home'),
    url(r'^home-one/(?P<slug>[\w-]+)$', 'app_hasjob.views.home_one', name='home_one'),
    url(r'^employee-form/$', 'app_hasjob.views.employee_form', name='employee_form'),

# ----------------------------- End Employee Details -----------------------------------------

# ----------------------------- Profile Details -----------------------------------------

    url(r'^profile/$', 'app_hasjob.views.profile', name='profile'),
    url(r'^edit-profile/$', 'app_hasjob.views.edit_profile', name='edit_profile'),
    url(r'^change-password/$', 'app_hasjob.views.change_password', name='change_password'),
    url(r'^add-email/$', 'app_hasjob.views.add_email', name='add_email'),
    url(r'^add-number/$', 'app_hasjob.views.add_number', name='add_number'),
    url(r'^client-application/$', 'app_hasjob.views.client_application', name='client_application'),
    url(r'^add-organization/$', 'app_hasjob.views.add_organization', name='add_organization'),

# ----------------------------- End Profile Details -----------------------------------------

# ----------------------------- Employer Details -----------------------------------------

    url(r'^add-job-post/$', 'app_hasjob.views.add_job_post', name='add_job_post'),
    url(r'^review/$', 'app_hasjob.views.review', name='review'),
    url(r'^edit-post/$', 'app_hasjob.views.edit_post', name='edit_post'),
    url(r'^confirm/$', 'app_hasjob.views.confirm', name='confirm'),
    url(r'^application-list/$', 'app_hasjob.views.application_list', name='application_list'),
    url(r'^application-one/(?P<slug>[\w-]+)$', 'app_hasjob.views.application_one', name='application_one'),

# ----------------------------- End Employer Details -----------------------------------------

# ----------------------------- Auth Details -----------------------------------------

    url(r'^signup/$', 'app_hasjob.views.signup', name='signup'),
    url(r'^signin/$', 'app_hasjob.views.signin', name='signin'),
    url(r'^logout/$', 'app_hasjob.views.logout', name='logout'),

# ----------------------------- End Auth Details -----------------------------------------

)
