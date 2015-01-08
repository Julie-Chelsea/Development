from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline (admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin (admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date info', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	search_fields = ['question_text']

# w/o modifications
# class QuestionAdmin(admin.ModelAdmin):
# 	#fields = ['question_text', 'pub_date']
# 	fieldsets = [
# 		(None,				{'fields': ['question_text']}),
# 		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
# 	]
# Register your models here.
admin.site.register(Question, QuestionAdmin)