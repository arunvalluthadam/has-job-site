from django import template
from .models import *

register = template.Library()

@register.inclusion_tag("tags/job_filter.html")
def job_filter(request):
	user = Signup.objects.get(username=request.user.username)
	return {'user': user}