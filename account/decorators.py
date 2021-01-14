from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.http import HttpResponse

def login_forbidden(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous, 
        login_url='/',    
        
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


def unauthenticated_user(func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('blog_app:home')
		else:
			return redirect('account_app:password-reset')

		view_func(request, *args, **kwargs)
	return wrapper_func