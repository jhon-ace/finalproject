from django.db import models

# Create your models here.
class user(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.IntegerField(max_length=30)