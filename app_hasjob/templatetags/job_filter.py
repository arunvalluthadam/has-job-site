from django import template
from app_hasjob.models import *
from app_hasjob.forms import *
from django.http import HttpResponseRedirect

register = template.Library()

@register.inclusion_tag("tags/job_filter.html")
def job_filter(request):
	filter_form = JobFilterForm(request.GET)
	return {'filter_form': filter_form}