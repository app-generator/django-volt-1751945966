# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Kso Chandigarh(models.Model):

    #__Kso Chandigarh_FIELDS__
    kso chandigarh = models.TextField(max_length=255, null=True, blank=True)
    text = models.TextField(max_length=255, null=True, blank=True)

    #__Kso Chandigarh_FIELDS__END

    class Meta:
        verbose_name        = _("Kso Chandigarh")
        verbose_name_plural = _("Kso Chandigarh")


class Kso Chandigarh Website(models.Model):

    #__Kso Chandigarh Website_FIELDS__
    kso chd = models.CharField(max_length=255, null=True, blank=True)

    #__Kso Chandigarh Website_FIELDS__END

    class Meta:
        verbose_name        = _("Kso Chandigarh Website")
        verbose_name_plural = _("Kso Chandigarh Website")



#__MODELS__END
