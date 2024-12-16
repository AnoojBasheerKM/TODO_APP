from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    phone = models.CharField(max_length=10,unique=True)
    
class Todo(models.Model):
    
    title = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=False)
    
    # cascade = delete the todo's of the user 
    # DO_NOTHING = nothing
    # SET_NUll = 

    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    


    
