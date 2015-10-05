
from django.db import models

class GroupUser(models.Model):

    title = models.CharField(max_length=255)
    position_id = models.ForeignKey()