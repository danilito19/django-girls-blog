from django.db import models
from django.utils import timezone

#each class I create is a table in my database
#and the functions and methods are column names
# make sure to go tell django that I created this model
# by using makemigratios command and then migrate command

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title