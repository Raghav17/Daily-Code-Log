from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30,default='SOME STRING')
    last_name = models.CharField(max_length=30,default='SOME STRING')
    email = models.CharField(max_length=30,default='SOME STRING')
    def __str__(self):
        return self.first_name
 