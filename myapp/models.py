from email.policy import default
from django.db import models

# Create your models here.
class Upload_image(models.Model):
    imgid = models.AutoField(primary_key=True)
    
    image = models.ImageField(default = "default.png", upload_to="images")
    

class Profile_card(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    images = models.ImageField(default = "default.png", upload_to="images")
    
class Pr_card(models.Model):
    prid = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    userid = models.ForeignKey(Profile_card, on_delete=models.CASCADE)
    