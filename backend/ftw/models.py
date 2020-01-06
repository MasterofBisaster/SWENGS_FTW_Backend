from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField(null=True)
    location = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    max_users = models.PositiveIntegerField()
    confirmed_users = models.ManyToManyField('User', related_name='attending_events', blank=True)
    costs = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class FTWUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('User', blank=True)

    def __str__(self):
        return self.user


class Location(models.Model):
    name = models.TextField()
    street = models.TextField()
    zip_code = models.PositiveIntegerField(max_length=5, null=True)
    country = models.TextField()
    max_user = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()

    def __str__(self):
        return self.creator


class Category(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class FTWWord(models.Model):
    CHOICES = (
        ('f', 'F'),
        ('t', 'T'),
        ('w', 'W')
    )
    word = models.TextField()

    def __str__(self):
        return self.word
