from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    date_created = models.DateTimeField(auto_now=True)

    def _str_(self):
        return "%s" % self.username
