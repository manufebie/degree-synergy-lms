from django.conf import settings
from django.db import models


class Project(models.Model):
    '''
    Projects represents a company project
    '''
    # client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
