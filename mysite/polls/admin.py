from django.contrib import admin

# Register your models here.
from polls.models import Poll


from polls.models import Choice
#admin.site.register(Poll)

# class PollAdmin(admin.ModelAdmin):
# 	fields = ['pub_date', 'question']

class ChoiceInline(admin.TabularInline): 
	model = Choice
	extra = 3 #sets default fields to 3

class PollAdmin(admin.ModelAdmin): #creates an admin
	fieldsets = [	
		(None,				{'fields': ['question']}), #creates field with no name
		('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}), #creates field with name
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin) #registers admin page


admin.site.register(Choice)


