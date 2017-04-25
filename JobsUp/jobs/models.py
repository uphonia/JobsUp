from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
	company_name = models.CharField(max_Length = 200, null = True)
	area_of_interest = models.CharField(max_Length = 200, null = True)
	phone_num = models.CharField(max_Length = 200, null = True)
	address = models.CharField(max_Length = 200, null = True)
	website = models.CharField(max_Length = 200, null = True)
	corpse = models.IntegerField()

	def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def update_user_profile(sender, instance, created, **kwargs):
	if created:
        Profile.objects.create(user=instance)
    instance.profile.save()