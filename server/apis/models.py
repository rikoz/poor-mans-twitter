from django.db import models

class PoorMansTweet(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "name"]
