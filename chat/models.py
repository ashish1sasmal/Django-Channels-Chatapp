from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatGroup(models.Model):
	groupname = models.CharField(max_length=20)
	user1 = models.ForeignKey(User,related_name="user1",on_delete=models.CASCADE,blank=False,null=False,default=None)
	user2  = models.ForeignKey(User,related_name="user2",on_delete=models.CASCADE,blank=False,null=False,default=None)

	def __str__(self):
		return self.groupname

class Message(models.Model):
	text = models.TextField(max_length=200, blank=True)
	fromUser = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
	toGroup = models.ForeignKey(ChatGroup,on_delete=models.CASCADE,blank=False,null=False)

	timestamp = models.DateTimeField(auto_now_add=True, blank=False)

	def __str__(self):
		return self.fromUser.username+"_"+self.toGroup.groupname+"_"+str(self.timestamp)