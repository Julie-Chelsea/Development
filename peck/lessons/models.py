from django.db import models
from django.utils import timezone

class Lesson (models.Model):
	number = models.PositiveIntegerField ('Lesson #', default = 0)
	title = models.CharField ('Lesson', max_length = 30)
	url = models.URLField(default = '', blank=True)
	k = 'KOR'
	j = 'JPN'
	language_choices = (
		(k, 'Korean'),
		(j, 'Japanese'),
		)
	language = models.CharField ('Language', max_length = 30, choices = language_choices, default = 'Korean')
	published = models.DateTimeField ('Date published', default = timezone.now)
	visible = models.BooleanField ('Show?', default = False)
	def __str__ (self):
		return self.title

class Word (models.Model):
	lesson = models.ForeignKey (Lesson)
	word = models.CharField ('Word/Phrase', max_length = 200)
	romanization = models.CharField(max_length = 200, default='', blank=True)
	definition_one = models.CharField ('Definition 1', max_length = 200, default='')
	def_2_exist = models.BooleanField('Another definition?', default = False)
	definition_two = models.CharField ('Definition 2', max_length = 200, default='', blank=True)
	def_3_exist = models.BooleanField('Another definition?', default = False, blank=True)
	definition_three = models.CharField ('Definition 3', max_length = 200, default='', blank=True)
	speech_level = models.CharField (max_length = 200, default='-')
	img = models.URLField(blank=True)
	help_text = "URL default format: img/lesson/k001/01.svg"
	def __str__ (self):
		return self.word

# class Quiz (models.Model):
# 	lesson = models.OneToOneField (Lesson, primary_key = True)
# 	def __str__ (self):
# 		return self.lesson

# # Types of questions
# # Matching
# class Matching_Question (models.Model):
# 	quiz = models.ForeignKey (Quiz)
# 	instruction = models.CharField ('Instructions', max_length = 200)
# 	def __str__ (self):
# 		return self.instruction

# class Pair1 (models.Model):
# 	question = models.ForeignKey (Matching_Question)
# 	item = models.CharField ('Pair 1', max_length = 100)
# 	def __str__ (self):
# 		return self.item

# class Pair2 (models.Model):
# 	question = models.ForeignKey (Pair1)
# 	item = models.CharField ('Pair 2', max_length = 100)
# 	def __str__ (self):
# 		return self.item

# #Short translate
# class Short_Translate_Question (models.Model):
# 	quiz = models.ForeignKey (Quiz)
# 	instruction = models.CharField ('Instructions', max_length = 200, default = "Translate the word/phrase into English.")
# 	question = models.CharField ('Question', max_length = 200)
# 	def __str__ (self):
# 		return self.question

# class Short_Translate_Answer (models.Model):
# 	question = models.ForeignKey (Short_Translate_Question)
# 	answer = models.CharField ('Potential answer', max_length = 200)
# 	def __str__ (self):
# 		return self.answer

# #Long translate
# class Long_Translate_Question (models.Model):
# 	quiz = models.ForeignKey (Quiz)
# 	instruction = models.CharField ('Instructions', max_length = 200, default = "Translate the word/phrase into English.")
# 	question = models.CharField ('Question', max_length = 200)
# 	def __str__ (self):
# 		return self.question

# class Long_Translate_Answer (models.Model):
# 	question = models.ForeignKey (Long_Translate_Question)
# 	answer = models.CharField ('Potential answer', max_length = 200)
# 	def __str__ (self):
# 		return self.answer

# # Fill-in-the-blanks
# class Fill_In_Blank_Question (models.Model):
# 	quiz = models.ForeignKey (Quiz)
# 	instruction = models.CharField ('Instructions', max_length = 200, default = "Fill in the blanks with the correct answer.")
# 	question = models.CharField ('Question', max_length = 500)
# 	def __str__ (self):
# 		return self.question

# class Fill_In_Blank_Answer (models.Model):
# 	question = models.ForeignKey (Fill_In_Blank_Question)
# 	answer = models.CharField ('Potential answer', max_length = 50)
# 	def __str__ (self):
# 		return self.answer

# # Video
# class Video (models.Model):
# 	quiz = models.ForeignKey (Quiz)	
# 	URL = models.URLField(default = "http://")
# 	instruction = models.CharField ('Instructions', max_length = 200, default = "Play the clips and answer the question(s).")
# 	def __str__ (self):
# 		return self.URL

# class Video_Question (models.Model):
# 	video = models.ForeignKey (Video)
# 	start_time = models.CharField (max_length = 10, default = "00:00:00")
# 	stop_time = models.CharField (max_length = 10, default = "00:00:00")
# 	question = models.CharField (max_length = 200)
# 	def __str__ (self):
# 		return self.question

# class Video_Answer (models.Model):
# 	question = models.ForeignKey (Video_Question)
# 	answer = models.CharField ('Potential answer', max_length = 200)
# 	def __str__ (self):
# 		return self.answer

# # True or false
# class True_False_Question (models.Model):
# 	quiz = models.ForeignKey (Quiz)
# 	question = models.CharField (max_length = 200)
# 	true = models.BooleanField ('True?', default = False)
# 	def __str__ (self):
# 		return self.question

# # Multiple choice
# class Multiple_Choice_Question (models.Model):
# 	quiz = models.ForeignKey (Quiz)
# 	question = models.CharField (max_length = 200)
# 	def __str__ (self):
# 		return self.question

# class Multiple_Choice_Answer (models.Model):
# 	question = models.ForeignKey (Multiple_Choice_Question)
# 	answer = models.CharField ('Option', max_length = 200)
# 	correct = models.BooleanField ('Correct?', default = False)
# 	def __str__ (self):
# 		return self.answer

# ####

# # Entertainment
# class Entertainment (models.Model):
# 	lesson = models.ForeignKey (Lesson)

# class Song (models.Model):
# 	entertainment = models.ForeignKey (Entertainment) # Songs = Subcategory of entertainment, and this represents that
# 	artist = models.CharField ('Artist', max_length = 50)
# 	name = models.CharField ('Song name', max_length = 100)
# 	URL = models.URLField(default = "http://")

# class Song_Genre (models.Model):
# 	song = models.ForeignKey (Song)
# 	genre = models.CharField ('Song genre', max_length = 50)

# class Drama (models.Model):
# 	entertainment = models.ForeignKey (Entertainment)