from django.db import models


class Input(models.Model):
    content = models.JSONField()

    def __str__(self):
        return self.content
