from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EN', 'Engineering'),
        ('BA', 'Business Administration'),
        ('ED', 'Education'),
        ('AS', 'Arts and Sciences'),
        ('AR', 'Architecture'),
        ('NU', 'Nursing'),
        ('MS', 'Maritime Studies'),
        ('OT', 'Other'),
    ]

    school_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username