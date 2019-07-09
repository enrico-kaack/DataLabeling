from django.db import models

# Create your models here.
class Content(models.Model):
    content = models.TextField()
    meta_data = models.TextField()

class Decision(models.Model):
    decisionNumber=models.IntegerField()
    content = models.ForeignKey(Content, on_delete=models.CASCADE)