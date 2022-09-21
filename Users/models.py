from django.db import models
from django.contrib.auth.models import User
from PIL import Image  #importing PILLOW module
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# dunder str method

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs): # overwrite the save method to reduce image size
        super().save(*args, **kwargs)          # parents class's save method will run first super() # this save method will run after our model is saved      
        img = Image.open(self.image.path)  # opening the image of current instance
        if img.height > 300 or img.width > 300 : 
            output_size = (300, 300)    # if h or w  > 300 then resize to 300x300 image
            img.thumbnail(output_size) # resize 
            img.save(self.image.path)  # save to the original path and overwrite the large image