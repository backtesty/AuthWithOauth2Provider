from django.db import models
from django.contrib.auth.models import User

# username, password, email, first_name, last_name, is_active, is_staff, is_superuser, last_login, date_joined

class Profile(models.Model):
    """
    Model to store extra information about the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50, blank=True, null=True) # Provider name (Google, Github, etc)
    token_details = models.TextField(blank=True, null=True) # Token details JSON format
    avatar = models.URLField(blank=True, null=True) # URL to the user's profile picture
    extra_info = models.TextField(blank=True, null=True) # Information about the user JSON format
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
