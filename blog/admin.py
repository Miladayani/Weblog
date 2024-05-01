from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_time_modified')


admin.site.register(Post, PostAdmin)
