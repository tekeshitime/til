from django.db import models

class List(models.Model):
    list_item = models.CharField(max_length=200)

    def __str__(self):
        return self.list_item