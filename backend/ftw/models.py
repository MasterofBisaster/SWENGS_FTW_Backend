from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class Location(models.Model):
    name = models.TextField()
    street = models.TextField(null=True)
    zip_code = models.PositiveIntegerField(null=True)
    country = models.TextField(null=True)
    max_user = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'events')
    private = models.BooleanField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name= 'events')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'events')
    description = models.TextField()
    max_users = models.PositiveIntegerField(null=True)
    confirmed_users = models.ManyToManyField(User, related_name='attending_events', blank=True)
    costs = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class FTWUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    def __str__(self):
        return self.user


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.creator.name + ': ' + self.content


class FTWWord(models.Model):
    CHOICES = (
        ('f', 'F'),
        ('t', 'T'),
        ('w', 'W')
    )
    word = models.TextField()
    word_category = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.word
