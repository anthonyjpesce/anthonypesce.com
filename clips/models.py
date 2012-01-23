from django.db import models
from django.conf import settings

class Clip(models.Model):
    """
    A fancy project to show off
    """
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/')
    url = models.URLField()
    CLIP_TYPE_CHOICES = (('Development', 'Development'), ('Writing', 'Writing'))
    clip_type = models.CharField(max_length=100, choices=CLIP_TYPE_CHOICES)
    project_date = models.DateField()
    
    class Meta:
        ordering = ('-project_date',)