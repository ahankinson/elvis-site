from django.db import models


class Tag(models.Model):
    old_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.name)

    class Meta:
        app_label = "elvis"
