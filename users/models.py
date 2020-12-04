from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
    	return f'{self.user.username} Profile'



class Friends(models.Model):
 	user1 = models.ForeignKey(Profile,related_name="prof1", on_delete=models.CASCADE)
 	user2 = models.ForeignKey(Profile,related_name="prof2", on_delete=models.CASCADE)

 	def __str__(self):
 		return f'{self.user1.user.username}_{self.user2.user.username}'

