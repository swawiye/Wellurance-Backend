from django.db import models

# Create your models here.
class Register(models.Model):
    # Equivalent to creating fields in a table
    fName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fName
    
class LogIn(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    fName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.DateField(max_length=100) #make this inactive
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fName