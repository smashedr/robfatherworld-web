from django.contrib import admin
from videos.models import Videos


@admin.register(Videos)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('category', 'title', 'video_id', 'created_at')
