from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): 
	email = forms.EmailField(required=True)        #default is require=true email must enter

	class Meta: 
		# when form.save() meta is going to save data to the User model
		model = User
		# order of saving the data in the form
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):    #this form allow us to update our User Profile
	email = forms.EmailField(required=True)        #default is require=true email must enter

	class Meta: 
		# when form.save() meta is going to save data to the User model
		model = User     #updating on 'User' model
		# order of saving the data in the form
		fields = ['username', 'email']  # updating on fields in 'User' models

class ProfileUpdateForm(forms.ModelForm):	# this form allow us to update our profile picture
	class Meta:
		model = Profile    #updating on 'Profile' model
		fields = ['image'] # updating on field in 'Profile' model