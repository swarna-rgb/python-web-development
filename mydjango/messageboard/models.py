from django.db import models

# Create your models here.

class MessageBoard(models.Model):
    posted_msg = models.TextField(default="")

    """def __str__(self):
        return self.posted_msg"""

