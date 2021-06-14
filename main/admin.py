from django.contrib import admin
from .models import Tutorial
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Content", {"fields": ["tutorial_content"]})
	]

admin.site.register(Tutorial, TutorialAdmin)