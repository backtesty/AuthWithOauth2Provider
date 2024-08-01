import json
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from .utils import google_oauth2, github_oauth2, linkedin_oauth2
from .models import Profile
# Create your views here.

class ProfileView(TemplateView):
    template_name = 'app_users/profile.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return super().get(request, *args, **kwargs)

class LoginView(TemplateView):
    template_name = 'app_users/login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        
        provider = request.GET.get('provider')
        if provider == 'google':
            auth_url, state = google_oauth2.get_auth_url()
            request.session['state'] = state
            return redirect(auth_url)
        elif provider == 'github':
            auth_url, state = github_oauth2.get_auth_url()
            request.session['state'] = state
            return redirect(auth_url)
        elif provider == 'linkedin':
            auth_url, state = linkedin_oauth2.get_auth_url()
            print(auth_url)
            request.session['state'] = state
            return redirect(auth_url)
        return super().get(request, *args, **kwargs)

class GoogleCallbackView(TemplateView):

    def get(self, request, *args, **kwargs):
        if request.GET.get('state') != request.session.get('state'):
            messages.error(request, 'Invalid state')
            return redirect('users:login')
        token = google_oauth2.get_token(request.GET.get('code'))

        if token is None:
            messages.error(request, 'Invalid token')
            return redirect('users:login')
        
        user_info = google_oauth2.get_user_info()
        
        email = user_info.get('email')
        given_name = user_info.get('given_name')
        family_name = user_info.get('family_name')
        picture = user_info.get('picture')
        provider = 'Github'

        if User.objects.filter(username=email).exists():
            user = get_object_or_404(User, username=email)
        else:
            user = User.objects.create_user(username=email, email=email,\
                                                first_name=given_name, last_name=family_name)
            Profile.objects.create(user=user, token_details=token, provider=provider,\
                                                 avatar = picture, extra_info=json.dumps(user_info))
        login(request, user)
        messages.success(request, 'Welcome {}'.format(user.first_name))
        return redirect('users:profile')
    
    def post(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def put(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def delete(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def patch(self, request, *args, **kwargs):
        return redirect('users:login')
    
class GithubCallbackView(TemplateView):
        
    def get(self, request, *args, **kwargs):
        if request.GET.get('state') != request.session.get('state'):
            messages.error(request, 'Invalid state')
            return redirect('users:login')
        token = github_oauth2.get_token(request.GET.get('code'))

        if token is None:
            messages.error(request, 'Invalid token')
            return redirect('users:login')
    
        user_info = github_oauth2.get_user_info(token.get('access_token'))
        
        email = user_info.get('email')
        name = user_info.get('name')
        avatar = user_info.get('avatar_url')
        provider = 'Github'
        
        if User.objects.filter(username=email).exists():
            user = get_object_or_404(User, username=email)
        else:
            user = User.objects.create_user(username=email, email=email,\
                                                first_name=name)
            Profile.objects.create(user=user, token_details=token, provider=provider,\
                                                avatar = avatar, extra_info=json.dumps(user_info))
        login(request, user)
        messages.success(request, 'Welcome {}'.format(user.first_name))
        return redirect('users:profile')
    
    def post(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def put(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def delete(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def patch(self, request, *args, **kwargs):
        return redirect('users:login')

class LinkedinCallbackView(TemplateView):
            
    def get(self, request, *args, **kwargs):
        if request.GET.get('state') != request.session.get('state'):
            messages.error(request, 'Invalid state')
            return redirect('users:login')
        
        token = linkedin_oauth2.get_token(request.GET.get('code'))

        if token is None:
            messages.error(request, 'Invalid token')
            return redirect('users:login')
        
        user_info = linkedin_oauth2.get_user_info(token.get('access_token'))

        email = user_info.get('email')
        name = user_info.get('name')
        avatar = user_info.get('avatar_url')
        provider = 'Linkedin'
        
        if User.objects.filter(username=email).exists():
            user = get_object_or_404(User, username=email)
        else:
            user = User.objects.create_user(username=email, email=email,\
                                                first_name=name)
            Profile.objects.create(user=user, token_details=token, provider=provider,\
                                                avatar = avatar, extra_info=json.dumps(user_info))
        login(request, user)
        messages.success(request, 'Welcome {}'.format(user.first_name))
        return redirect('users:profile')
    
    def post(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def put(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def delete(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def patch(self, request, *args, **kwargs):
        return redirect('users:login')

class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'You have been logged out')
        return redirect('users:login')
    
    def post(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def put(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def delete(self, request, *args, **kwargs):
        return redirect('users:login')
    
    def patch(self, request, *args, **kwargs):
        return redirect('users:login')
