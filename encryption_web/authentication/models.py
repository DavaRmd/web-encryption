from django.db import models

# Create your models here.

class User(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,  unique=True)
    no_hp = models.CharField(max_length=13,  unique=True)
    nip = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_profile'