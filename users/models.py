from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    phone = models.CharField(max_length=10, default="0000000000")
    def __str__(self):
    	return f'{self.user.username} Profile'

    # def save(self):
    # 	super().save()
    # 	img=Image.open(self.image.path)
    #
    # 	if img.height>300 or img.width>300:
    # 		output_size=(300,300)
    # 		img.thumbnail(output_size)
    # 		img.save(self.image.path)



class Friends(models.Model):
 	user1 = models.ForeignKey(Profile,related_name="prof1", on_delete=models.CASCADE)
 	user2 = models.ForeignKey(Profile,related_name="prof2", on_delete=models.CASCADE)

 	def __str__(self):
 		return f'{self.user1.user.username}_{self.user2.user.username}'
