
from .models import Post
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class PostAddForm(forms.ModelForm):
	title = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":""}))
	description = forms.CharField(label="", help_text="", widget=forms.Textarea(attrs={"class":"form-control","placeholder":""}))

	class Meta:
		model = Post
		fields = ('title', 'description', 'image')



class PostUpdateForm(forms.ModelForm):
	title = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":""}))
	description = forms.CharField(label="", help_text="", widget=forms.Textarea(attrs={"class":"form-control","placeholder":""}))

	class Meta:
		model = Post
		fields = ('title', 'description', 'image')

