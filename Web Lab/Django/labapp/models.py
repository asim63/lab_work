from django.db import models

#for question 1
class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    
#question 2
class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    dob = models.DateField()
    doctor_name = models.CharField(max_length=100)
    
# #question 6
# class Note(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
    
from django.core.exceptions import ValidationError
def validate_content_length(value):
    if len(value) < 10:
        raise ValidationError(
            "Description must be at least 10 characters long.")

class Note(models.Model):
    title      = models.CharField(max_length=200)
    content    = models.TextField(validators=[validate_content_length])
    created_at = models.DateTimeField(auto_now_add=True)