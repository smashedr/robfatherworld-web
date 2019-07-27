from django.contrib import admin
from videos.models import Videos


@admin.register(Videos)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('title', 'video_id', 'category', 'created_at')
