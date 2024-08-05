from django.db import models
#from django.contrib.auth.models import User                     
#import the builtin users from django admin panel{no longer using this, using custom model}

# Create your models here.

# (use python3 manage.py makemigrations[makes migrations], 
# followed by python3 manage.py migrate[applies migrations]
# after inserting the required content below
# Note: this process needs to be done everytime there is any change in the db structure)

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True, default="Hey, there I'm using PhysiXplorer!")
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Room(models.Model):                                       #inherit from models
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank= True)      # can be null in db, field is optional in forms
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)               # makes a note of the timestamp of model updation
    created = models.DateTimeField(auto_now_add=True)           # makes a note of whenever the model was added(created)

    class Meta:
        ordering = ['-created', '-updated']                     # (arranges the content in the descending order 
                                                                # i.e, newly created/updated rooms appear at the top)

    def __str__(self):
        return str(self.name)
    
class Message(models.Model):                                   # one room has multiple messages
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # if a user is deleted, delete all messages sent by that user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)   # if a room is deleted, delete all messages in that room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)               # makes a note of the timestamp of model updation
    created = models.DateTimeField(auto_now_add=True)           # makes a note of whenever the model was added(created)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return str(self.body[:50])                              # trim to 1st 50 characters