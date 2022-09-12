from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# creating user registeration form from django build in 

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid(): 
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Welcome {username}!, your account has been created! You are now able to log in!') #flash message when valid
			return redirect('login') #redirect to login page after account registration

	else: 
		form = UserRegisterForm()
	return render(request, 'Users/register.html', {'form': form, 'title': 'User Registration'})

@login_required
def profile(request):
	return render(request, 'Users/profile.html', {'title' : 'Profile'}     )



#message.debug
#message.info
#essage.success
#message.warning
#message.error