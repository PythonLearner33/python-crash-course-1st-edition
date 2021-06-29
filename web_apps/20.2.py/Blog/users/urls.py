from django.urls import path
# from django.contrib.auth.views import login # This is the view function we're using.
# from django.contrib.auth import login # Dont mistake login for this; this logs in the user.

# disregard above comments. it will give an import error b/c we are using a newer version.

from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('log_in/', LoginView.as_view(template_name='users/log_in.html'), name='log_in'),
]