from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
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

# funtion base view can be used with decorators 

@login_required
def profile(request): 
	if request.method == 'POST':   
		u_form = UserUpdateForm(request.POST, instance=request.user)  #pass in instance of the user 
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)     #pass in instance of the profile 
		
		if u_form.is_valid() and p_form.is_valid(): 
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated')
			return redirect('profile')

	else: 
		u_form = UserUpdateForm(instance=request.user)  #pass in instance of the user 
		p_form = ProfileUpdateForm(instance=request.user.profile)     #pass in instance of the profile 

	context = {
		'u_form' : u_form,
		'p_form' : p_form,
		'title'  : 'Profile',

	}
	return render(request, 'Users/profile.html', context)



#message.debug
#message.info
#essage.success
#message.warning
#message.error