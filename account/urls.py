#coding:utf-8

from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth.views import (
	LoginView,
	LogoutView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView

)
from django.contrib.auth.decorators import login_required
from account.decorators import login_forbidden, unauthenticated_user
from django.contrib.auth import views as auth_views


app_name = 'account_app'


urlpatterns = [
	path('login/', LoginView.as_view(template_name='account/login.html', redirect_authenticated_user=True), name="login"),
	path('logout/', login_required(LogoutView.as_view(template_name='account/logout.html')), name="logout"),
	path('signup/', views.SignUpView.as_view(), name="signup"),
	path('profile/', login_required(views.ProfileView.as_view()), name="profile"),
	path('profile-update/<username>/<int:pk>/', login_required(views.ProfileUpdateView.as_view()), name="profile-update"),
	path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
        template_name='account/change_password.html',
        success_url = reverse_lazy('account_app:profile')),
        name='change-password'
    ),

	path('password-reset/', login_forbidden(PasswordResetView.as_view(
		template_name='account/password_reset.html', 
		email_template_name='account/registration/password_reset_email.html', 
		subject_template_name='account/password_reset_subject.txt', 
		success_url=reverse_lazy('account_app:password-reset-done'))),name="password-reset"),
	path('password-reset-done/', 
		unauthenticated_user(PasswordResetDoneView.as_view(template_name='account/password_reset_done.html')),
		name="password-reset-done"),

	path('password-reset-confirm/<uidb64>/<token>/', 
		PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', 
		success_url=reverse_lazy('account_app:password-reset-complete')),
		name='password-reset-confirm'),
	path('password-reset-complete/', unauthenticated_user(PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html")), name="password-reset-complete")		  
];