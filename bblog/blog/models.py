# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Blog_Detail(models.Model):
	title = models.CharField(max_length=125)
	description=models.TextField(max_length=500)
	time_now=models.DateTimeField(timezone.now())
