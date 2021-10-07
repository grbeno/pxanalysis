from django.db import models

class TestModel(models.Model):
    test_name = models.CharField(max_length=30)
