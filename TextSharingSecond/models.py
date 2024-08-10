from django.db import models

class EnteredText(models.Model):
    entered_url = models.CharField(max_length=100)

    def __str__(self):
        return self.entered_url