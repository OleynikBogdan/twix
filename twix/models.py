from django.db import models


class Record(models.Model):
    record_text = models.TextField()