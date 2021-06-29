from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # When login/ is requested, use default login view with template passed in to render to user.
    # login view can handle post and get requests. same as the other form views in learning_logs.
    path('logout/', views.logout_view, name='logout'), # there is LogoutView as well, which works.
    path('register/', views.register, name='register'),
]