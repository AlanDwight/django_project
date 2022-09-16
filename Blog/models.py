#making database fields 
#developing with mysql and production with postgresql

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)					#title length 
	content = models.TextField()									# content field  	
	date_posted = models.DateTimeField(default = timezone.now)		#update date on creating the post
	author = models.ForeignKey(User, on_delete = models.CASCADE) #delete the post as well on deleting the user


	def __str__(self): 
		return self.title	

	def get_absolute_url(self): 
		return reverse('Blog:post-detail', kwargs={'pk': self.pk})