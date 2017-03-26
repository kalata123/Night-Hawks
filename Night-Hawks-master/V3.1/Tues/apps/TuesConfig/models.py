from django.db import models


class Test(models.Model):
    Message = models.CharField(max_length=30,default="")
    Keyword = models.CharField(max_length=30, default="")
    Answer = models.CharField(max_length=30, default="",)

# Create your models here.
