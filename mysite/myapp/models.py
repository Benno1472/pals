from django.db import models
from django.utils import timezone
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block

# Create your models here.
# find person first, then get posts though ID
# from myapp.models import Person, Comment, Post, Schedule
# To make a object object_name(var_name="info" ... )
# e.g Person(person_name="bob",person_text="the builder")
# To add a item, Person_object.Post_set.create()
# Works the same with the comment and post

# f1 = Friends(source=user1,target=user2)
# f1.save()
# see friends_list with p1.friends_list.all()
# should be good

class Person(models.Model):
    person_name = models.CharField(max_length=20, default="")
    person_text = models.CharField(max_length=200, default="")
    friends_list = models.ManyToManyField('self', through = 'Friends',
          symmetrical = False)


    class Meta:
        ordering = ['person_name']
    def __str__(self):
        return self.person_name

class Friends(models.Model):
    source = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'source', on_delete=models.CASCADE,default=None)
    target = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'target', on_delete=models.CASCADE, default=None)


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    print("uploading")
    post_img = models.ImageField(
        upload_to=None, default="No picture")
    post_text = models.CharField(max_length=200, default="no text")
    # when you are getting this date, remeber to subtract to get time since last
    posted_time = models.DateTimeField("previous time")

    post_used = 0

    def __str__(self):
        return self.post_text
class Schedule(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, default="Nobody")
    schedule_item = models.CharField(max_length=200, default="no text")
    schedule_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.schedule_item, self.schedule_time


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    comment_text = models.CharField(max_length=200, default="")

    def return_info(self):
        return self.comment_text
