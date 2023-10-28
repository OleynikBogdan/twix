from django.db import models


class Record(models.Model):
    record_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.record_text
    