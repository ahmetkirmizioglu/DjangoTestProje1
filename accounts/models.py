from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    bio  = models.TextField(null=True, blank=True)
    type = models.PositiveIntegerField(null=True, blank=True)
    applications = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profil'