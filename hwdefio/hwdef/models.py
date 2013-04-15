from django.db import models


class Hardware(models.Model):

    text = models.TextField(
        help_text="This field is free form, fire your creativity!")
