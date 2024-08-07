from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

	#-----------------Chat-----------------#
	path('', views.home, name='home'),
	path('chat/', views.chat, name='chat'),
	path('chat/<str:username>/<int:id>/', views.chat_room, name='chat_room'),

	#-----------------Contacts-----------------#
	path('contacts/friends/', views.contacts, name='contacts'),
	path('contacts/friend-request/', views.friend_request, name='friend_request'),
	path('contacts/friend-request-send/', views.friend_request_send, name='friend_request_send'),

	#-----------------Profile-----------------#
	path('profile/', views.profile, name='profile'),
	path('edit-profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
	path('edit-avatar/<int:user_id>/', views.change_avatar, name='edit_avatar'),
	path('contact-profile/<str:username>/<int:id>/', views.contact_profile, name ='contact_profile'),

	#-----------------Authentication-----------------#
	path('accounts/login/', views.sign_in, name='login'),
	path('accounts/signup/', views.sign_up, name='signup'),
	path('accounts/logout/', views.logout_user, name='logout'),

	#-----------------Email Verification-----------------#
	path('verification/', include('verify_email.urls')),
	path('verification/msg/', views.verification_msg, name='verification_msg'),

	#-----------------Password Reset-----------------#
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='forgot_password/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='forgot_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='forgot_password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='forgot_password/password_reset_complete.html'), name='password_reset_complete'),

	#-------------------Password Change-------------------#
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change/password_change_done.html'), name='password_change_done'),

	#-------------------Forgot Username-----------------#
	path('forgot-username/', views.forgot_username, name='forgot_username'),



	#-------------------Friend Request-----------------#
	path('send-request/<int:user_id>/', views.send_request, name='send_request'),
	path('accept-request/<int:user_id>/', views.accept_request, name='accept_request'),
	path('reject-request/<int:user_id>/', views.reject_request, name='reject_request'),
	path('cancel-request/<int:user_id>/', views.cancel_request, name='cancel_request'),
]