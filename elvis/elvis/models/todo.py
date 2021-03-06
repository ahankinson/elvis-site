from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey("elvis.Project")
    assigned_to = models.ForeignKey(User, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    created = models.DateTimeField(default=datetime.now, blank=True)


    def __unicode__(self):
        return u"{0}".format(self.project)

    class Meta:
        app_label = "elvis"
