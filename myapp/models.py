# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user=models.OneToOneField(User)


    portfolioLink=models.URLField(blank=True)
    profile_pic=models.ImageField(blank=True,upload_to="profile_pics")


    def __str__(self):
        return self.user.username
