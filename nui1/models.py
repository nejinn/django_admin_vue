from django.db import models


# Create your models here.
class Test1(models.Model):
    name = models.CharField("测试1", max_length=225, default=None, null=True, blank=True)
