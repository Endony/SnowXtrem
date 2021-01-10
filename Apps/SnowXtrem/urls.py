from django.urls import path
from .views import edit, home, register, news, parks, gallery
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'SnowXtrem'

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('home/', home, name='home'),
    path('news/', news, name='news'),
    path('parks/', parks, name="parks"),
    path('gallery/', gallery, name="gallery"),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='snowxtrem/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='snowxtrem/password_change_form.html', success_url=reverse_lazy('snowxtrem:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='snowxtrem/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='snowxtrem/password_reset_form.html',
        email_template_name='snowxtrem/password_reset_email.html',
        success_url=reverse_lazy('snowxtrem:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='snowxtrem/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='snowxtrem/password_reset_confirm.html',
        success_url=reverse_lazy('registration:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='snowxtrem/password_reset_complete.html'), name='password_reset_complete'),

]
