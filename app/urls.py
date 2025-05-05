from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  register, IndexView, Create, Edit, Delete


urlpatterns = [
    # auth urls
    path('', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    path('register/', register, name="register"),
    
    #app_urls
    path('index/', IndexView.as_view(), name="IndexView"),
    path('create/', Create.as_view(), name="Create"),
    path('edit/<int:pk>', Edit.as_view(), name ="edit"), 
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
]    