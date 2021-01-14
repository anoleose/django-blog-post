from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .forms import PostAddForm, PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class HomeView(ListView):
	def get(self, request):
		posts = Post.objects.all()

		context = {
			'posts':posts,
			
		}
		
		template = loader.get_template('blog/home.html')
		return HttpResponse(template.render(context, request))

class PostDetailView(DetailView):
	def get(self, request, title, id):
		post = get_object_or_404(Post, title=title, id=id)

		context = {
			'post':post,
		}

		template = loader.get_template('blog/post_detail.html')
		return HttpResponse(template.render(context, request))


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Post
	form_class = PostAddForm
	template_name = 'blog/add_post.html'
	success_message = 'Your post has been added'
	success_url = reverse_lazy('blog_app:home')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ('title', 'description', 'image')
	template_name = 'blog/post_update_form.html'
	success_message = 'Post was updated'
	success_url = reverse_lazy('account_app:profile')


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_message = 'Post deleted'
	success_url = reverse_lazy('account_app:profile')

	def test_func(self):
		Post = self.get_object()
		if self.request.user == Post.author:
			return True
		else:
			return False
