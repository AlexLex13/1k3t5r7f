from django.db import models

# Create your models here.


class Input(models.Model):
    content = models.JSONField()

    def __str__(self):
        return self.content
