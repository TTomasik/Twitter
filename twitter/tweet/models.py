from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from django.contrib.auth.models import AbstractUser
# Create your models here.

# class MyUser(AbstractUser):
#     avatar = models.ImageField(upload_to='static/pictures', null=True, blank=True)

class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/pictures', null=True, blank=True)

    def __str__(self):
        return '%s is %s' % (self.user.username, self.avatar)

class Tweet(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)


    def __str__(self):

        return 'DATE: %s, %s...' % (self.creation_date, str(self.content)[:32])

    """self.user.avatar,"""
    class Meta:
        ordering = ['-creation_date']

class Message(models.Model):
    sender = models.ForeignKey(User)
    receiver = models.ForeignKey(User, related_name="message_receiver")
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return 'Message from {} to {} @ {}'.format(self.sender, self.receiver, self.creation_date)


