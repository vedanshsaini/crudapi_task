from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    is_approved=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
class product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=15,decimal_places=5)
    user=models.ForeignKey(user,on_delete=models.CASCADE,related_name='user')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
