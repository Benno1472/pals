from django.db import models

# Create your models here.
class Person(models.Model):
    person_name = models.CharField(max_length=20)
    person_text = models.CharField(max_length=200)

    def __str__(self):
        return self.person_name


class Post(models.Model):
    #post_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    post_text = models.CharField(max_length=200)

    def __str__ (self):
        return self.post_text
