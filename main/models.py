from django.db import models
from datetime import datetime

# These become the columns in our database
# if you add or change anything here, you have to
# make migration and migrate. 2 distinct steps
# to make migration, in mysite directory run: python manage.py makemigrations
# to migrate, in mysite directory run: python manage.py migrate
# to get an interactive console to play with website, run: python manage.py shell

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.tutorial_title
