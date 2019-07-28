import logging
import re
from django.db import models

logger = logging.getLogger('app')


class Videos(models.Model):
    CATEGORY = [
        ('tutorials', 'Lunar Magic Tutorials'),
        ('speedruns', 'Robfather Speedruns'),
    ]
    HELP_TEXT = {
        'category': 'Which section the video will appear in.',
        'title': 'Title of the video.',
        'description': 'Description text about the video.',
        'video_id': 'Video URL or ID from the YouTube share button.',
    }

    category = models.CharField(max_length=255, choices=CATEGORY, default='tutorials', help_text=HELP_TEXT['category'])
    title = models.CharField(max_length=255, help_text=HELP_TEXT['title'])
    description = models.TextField(help_text=HELP_TEXT['description'])
    video_id = models.CharField(max_length=255, help_text=HELP_TEXT['video_id'])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        m = re.search('[a-zA-Z0-9\-\_]{8,20}', self.video_id)
        logger.info(m)
        self.video_id = m.group(0)
        logger.info(self.video_id)
        super(Videos, self).save()

    class Meta:
        verbose_name = 'Videos'
        verbose_name_plural = 'Videos'
