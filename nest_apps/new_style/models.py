from django.db import models


class NewStyle(models.Model):
    name = models.CharField('name', max_length=50)