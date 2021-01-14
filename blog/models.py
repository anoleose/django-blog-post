from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class PostManager(models.Manager):

    def public_posts(self, *args, **kwargs):
        return super(
            PostManager,
            self).filter(public=True)

    def private_posts(self, *args, **kwargs):
    	author = kwargs.pop('author')
    	return super(PostManager,self).filter(public=False, author=author)

class Post(models.Model):
	author           = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title           = models.CharField(max_length=120)  
	description     = models.TextField()
	image           = models.ImageField(upload_to='image/', null=True, blank=True, default='image/imageicon.png')
	active          = models.BooleanField(default=True)
	public          = models.BooleanField(default=False)
	private         = models.BooleanField(default=True)
	created_at      = models.DateTimeField(auto_now_add=True, auto_now =False)
	updated_at      = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = PostManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blog_app:post-detail", kwargs={'title': self.title, 'id': self.id})
	
	def get_update_url(self):
		return reverse("blog_app:update", kwargs={'title': self.title, 'pk': self.pk})

	def get_delete_url(self):
		return reverse("blog_app:delete", kwargs={'title': self.title, 'pk': self.pk})

	

	@property
	def get_image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url
		