import logging
import re
from django.db import models

logger = logging.getLogger('app')


class Videos(models.Model):
    CATEGORY = [
        ('tutorials', 'Tutorials'),
    ]
    category = models.CharField(max_length=255, choices=CATEGORY, default='tutorials')
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_id = models.CharField(max_length=255)
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
