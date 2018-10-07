from django.db import models
from django.db.models.functions import Now


class Conversion(models.Model):

    created_at = models.DateTimeField(default=Now())
    input_number = models.TextField(max_length=255, null=False)
    output_number = models.TextField(max_length=255, null=False)
