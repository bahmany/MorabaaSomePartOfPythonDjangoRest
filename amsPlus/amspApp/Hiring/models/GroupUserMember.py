from django.contrib.auth.models import User
from django.db import models
from amspApp.amspUser.h.GroupUser import GroupUser


class GroupUserMember(models.Model):
    
    user_id = models.ForeignKey(User)
    group_user_id = models.ForeignKey(GroupUser)