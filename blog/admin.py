from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']
	search_fields = ['title', 'description']
	date_hierarchy = 'created_at'
	list_filter = ['title', 'active']
	readonly_fields = ['updated_at', 'created_at']
	
	class Meta:
		model = Post
	
admin.site.register(Post, PostAdmin)