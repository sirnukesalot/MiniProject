from django.contrib import admin
from django.contrib.auth.models import User

from users.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile,ProfileAdmin)
