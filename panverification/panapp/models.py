# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from panapp.utils import get_upload_file_path
from panapp.constants import INVALID_CHOICES, FEEDBACK_CHOICES, PAN_CARD_STATUS, PENDING

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Agent(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)

	def __unicode__(self):
		return "agentdata"


class UserData(models.Model):
	image = models.FileField(upload_to=get_upload_file_path)
	extracted_name = models.CharField(max_length=50, blank=True, null=True)
	extracted_dob = models.CharField(max_length=12, blank=True, null=True)
	extracted_pan = models.CharField(max_length=10, blank=True, null=True)
	is_verified_agent = models.BooleanField(default=False)
	is_invalid_auto = models.BooleanField(default=False)
	is_verified_auto = models.BooleanField(default=False)
	is_scanned = models.BooleanField(default=False)
	error_msg = models.CharField(max_length=100, blank=True, null=True)
	user = models.ForeignKey(User, blank=True, null=True)
	agent = models.ForeignKey(Agent, blank=True, null=True)
	status = models.CharField(max_length=2, choices=PAN_CARD_STATUS,
								default=PENDING)

	def __unicode__(self):
		return str(self.id)


class FailedUserData(models.Model):
	user_data = models.ForeignKey(UserData)
	invalid = models.CharField(max_length=2, choices=INVALID_CHOICES)

class FeedbackData(models.Model):
	user_data = models.ForeignKey(UserData)
	feedback_for = models.CharField(max_length=2, choices=FEEDBACK_CHOICES)
	details = models.CharField(max_length=100)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

