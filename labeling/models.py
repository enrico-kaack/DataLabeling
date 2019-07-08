from django.db import models

# Create your models here.
class Content(models.Model):
    content = models.CharField(max_length=5192)
    meta_data = models.CharField(max_length=5192)

class Decision(models.Model):
    decisionNumber=models.IntegerField()
    content = models.ForeignKey(Content, on_delete=models.CASCADE)