import this

from django.db import models


# Create your models here.


class Diary(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isLocked = models.BooleanField(default=True)
    entries = []

    def __str__(self):
        return self.username


class Entry(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
