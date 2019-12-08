from django.utils import timezone
from django.db import models
from django.urls import reverse
from datetime import date

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
    owner = models.CharField(max_length=150)
    cost = models.CharField(max_length=100)
    shower = models.CharField(max_length=100)
    parking = models.CharField(max_length=100)
    locker_room = models.CharField(max_length=100)
    date_pub = models.DateTimeField('date_pulished', default=timezone.now())
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

