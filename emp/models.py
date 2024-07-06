from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=200)
    empId=models.CharField(max_length=10)
    empPhone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    department=models.CharField(max_length=20)
    
class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)
     
def __str__(self):
    return self.testimonial 
     