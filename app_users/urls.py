from .views import LoginView, ProfileView, LogoutView, GoogleCallbackView, GithubCallbackView, LinkedinCallbackView
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('auth/google/callback/', GoogleCallbackView.as_view(), name='google_callback'),
    path('auth/github/callback/', GithubCallbackView.as_view(), name='github_callback'),
    path('auth/linkedin/callback/', LinkedinCallbackView.as_view(), name='linkedin_callback'),
]   