from django.contrib import admin

# Register your models here.
from django.contrib import admin

from blog.models import (Post, Comment)


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)