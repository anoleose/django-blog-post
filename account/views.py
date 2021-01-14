from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin 
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from .forms import SignUpForm, ProfileUpdateForm, ChangePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from blog.models import Post
# Create your views here.


class SignUpView(CreateView):
	model = User
	form_class = SignUpForm
	template_name = 'account/signup.html'
	success_message = 'Your account has been created'
	success_url = reverse_lazy('account_app:login')

	@method_decorator(sensitive_post_parameters('password1', 'password2'))
	def dispatch(self, request, *args, **kwargs):   
		if request.user.is_authenticated:
			return redirect('blog_app:home')
		if not self.registration_allowed(request):
			return redirect(self.disallowed_url)
		return super(RegistrationView, self).dispatch(request, *args, **kwargs)



	def form_invalid(self, form):
		messages.warning(self.request, 'Your post has not been added'.format())
		return self.render_to_response(self.get_context_data(form=form))

class ProfileView(ListView):
	model = Post
	template_name = 'account/profile.html'

	def get(self, request, *args, **kwargs):
		posts = Post.objects.private_posts(author=request.user)
		return render(request, self.template_name, {'posts':posts})



class ProfileUpdateView(UpdateView):
	model = User
	form_class = ProfileUpdateForm
	template_name = 'account/user_update_form.html'
	success_message = 'Profile updated'
	success_url = reverse_lazy('account_app:profile')

	def get_object(self, queryset=None): 
		return self.request.user
		

