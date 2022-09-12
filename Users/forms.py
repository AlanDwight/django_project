from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): 
	email = forms.EmailField(required=True)        #default is require=true email must enter

	class Meta: 
		# when form.save() meta is going to save data to the User model
		model = User
		# order of saving the data in the form
		fields = ['username', 'email', 'password1', 'password2']