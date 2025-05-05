from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    initials = models.CharField(max_length=1, blank=True)
    firstname = models.CharField(max_length=200, blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    home = models.CharField(max_length=500, blank=True)
    company = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    work = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    note = models.TextField(max_length=60, blank=True)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'