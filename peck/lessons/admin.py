from django.contrib import admin
from lessons.models import Lesson, Word

class WordInline (admin.TabularInline):
	model = Word
	fields = ('word', 'romanization', 'speech_level', 'definition_one', 'def_2_exist', 'definition_two', 'def_3_exist', 'definition_three', 'img')
	extra = 0

class LessonAdmin (admin.ModelAdmin):
	fieldsets = [
	('Lesson information', {'fields': ['number']}),
	(None, {'fields': ['title']}),
	(None, {'fields': ['url']}),
	(None, {'fields': ['visible']}),
	(None, {'fields': ['language']}),
	# ('Date information', {'fields': ['published'], 'classes': ['collapse']}),
	]
	inlines = [WordInline]
	list_display = ('title', 'number', 'published')

admin.site.register(Lesson, LessonAdmin)