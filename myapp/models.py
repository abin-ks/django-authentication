from email.policy import default
from django.db import models

# Create your models here.
class Upload_image(models.Model):
    imgid = models.AutoField(primary_key=True)
    
    image = models.ImageField(default = "default.png", upload_to="images")