from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'bio', 'applications', 'type']

    class Meta:
        model = UserProfile

admin.site.register(UserProfile,UserProfileAdmin)