from django.db import models
from django.utils import timezone

# Create your models here.
# find person first, then get posts though ID
class Person(models.Model):
    person_name = models.CharField(max_length=20)
    person_text = models.CharField(max_length=200)
    post_list = [00000000]
    def add_id():
        pass
    def __str__(self):
        return self.person_name
class Comment:
    def __init__(self, person, text):
        self.person = person
        self.text = text
    def return_info():
        return self.person,self.text

class Post(models.Model):
    post_owner = "Person"
    post_id = 00000000
    post_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    post_text = models.CharField(max_length=200)
    posted_time = models.DateTimeField("previous time")  # when you are getting this date, remeber to subtract to get time since last
    comment_list = []
    def comment_add(text):
        comment_list.append(Comment(person, text))
    def __str__ (self):
        return self.post_text
