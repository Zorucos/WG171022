from django.db import models



# # Create your models here.
# class Profile(models.Model):
# 	user			= models.OneToOneField(User)
# 	followers		= models.ManzToManzField(User, related_name="", blank=True)
# 	activated 		= models.BooleanField(default=False)
# 	timestamp		= models.DateTimeField(auto_now_add=True)
# 	updated 		= models.DateTimeField(auto_now=True)

# 	objects = ProfileManager()

# 	def __str__(self):
# 		return self.user.username

# 	def send_activation_email(self):
# 		print("Activation")
# 		pass

