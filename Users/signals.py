# I create this files because everytime user sign up to my website they will be given a profile with default
# profile pics, so the user won't need to access to the admin page and create his/her own profile page.

from django.db.models.signals import post_save

# this is the signal fires after the object is save 
# post_save signal when the user is created 

from django.contrib.auth.models import User  # sender 
from django.dispatch import receiver # receiver will handle what sender send
from .models import Profile # object will create profile page for a created user

@receiver(post_save, sender=User)  # if user is created and saved, then send 'post_save' signal which is under
def create_profile(sender, instance, created, **kwargs):   # 'receiver' decorator that call the 'create_profile' function
	if created:												# with the all of the augments of 'post_save' signals and that funtion 
		Profile.objects.create(user=instance)			# create profile page everytime when each user is registered 



@receiver(post_save, sender=User) 				# function about saving profile after being created 
def save_profile(sender, instance, **kwargs):  # **kwargs just accept any additional keyword augment in the function
	instance.profile.save()				# instance is basically created_user's instance
										# instance is saving its profile


	# import signals in User/app.py file