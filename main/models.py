from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Task(models.Model):
    # user if many to many field bcz he/she may create many todo's
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="tasks") #related name is used to access to reverse way
    title = models.CharField(max_length=100) # title is mandatory
    description = models.TextField(null=True,blank=True) # this field is optional
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title 
