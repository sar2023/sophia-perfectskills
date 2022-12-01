from django.db import models
from django.db import models

# Create your models here.

class videoAns(models.Model):
    user_name = models.CharField(max_length=255,null=True)
    assessment_name = models.CharField(max_length=300,null=True)
    question = models.CharField(max_length=300,null=True)
    videoAns = models.FileField(upload_to='media',blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    

    def __str__(self):
        return self.user_name

