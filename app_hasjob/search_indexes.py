import datetime
from haystack import indexes
from .models import *

class AddJobPostIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	types = indexes.CharField(model_attr='types')
	category = indexes.CharField(model_attr='category')
	date = indexes.DateTimeField(model_attr='date')
	location = indexes.CharField(model_attr='location')

	content_auto = indexes.EdgeNgramField(model_attr='company')

	def get_model(self):
		return AddJobPost