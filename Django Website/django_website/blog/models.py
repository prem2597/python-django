from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    """Note:
    Keyword arguments: auto_now_add
    argument -- Here if we _add then we will not be able to change the date
    as per the users choice. So instead of _add we can simply use auto_now
    and assing that value as TRUE.
    Return: Current Date automatically.
    """
    date_posted = models.DateTimeField(default=timezone.now)
    """Bote:
    Keyword arguments: CASCADE
    argument -- If the user is deleted then all the posts related to the 
    User should also be deleted.
    Return: Deleted the posts related to the User on deletion of the User.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)





