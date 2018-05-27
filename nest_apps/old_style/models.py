from django.db import models


class OldStyle(models.Model):
    name = models.CharField('name', max_length=50)