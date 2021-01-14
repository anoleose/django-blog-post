from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=False, help_text='')
	first_name = forms.CharField(max_length=30, required=False, help_text='')
	last_name = forms.CharField(max_length=30, required=False, help_text='')
	email = forms.EmailField(max_length=254, help_text='')
	password1 = forms.CharField(required=True, label='password')
	password2 = forms.CharField(required=True, label='confirm password')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class ProfileUpdateForm(ModelForm):
	username = forms.CharField(max_length=30, required=False, help_text='')
	first_name = forms.CharField(max_length=30, required=False, help_text='')
	last_name = forms.CharField(max_length=30, required=False, help_text='')
	email = forms.EmailField(max_length=254, help_text='')
	
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')



class ChangePasswordForm(PasswordChangeForm):
	old_password = forms.CharField(required=False, help_text='')
	new_password1 = forms.CharField(label='new password', required=False, help_text='')
	new_password2 = forms.CharField(label='confirm password', required=False, help_text='')


	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')
	
