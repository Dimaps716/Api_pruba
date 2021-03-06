"""items"""
# Django
from django.db import models

# creation of the database model its fields and parameters
class items(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    picture_url = models.URLField(max_length=400)
    url_located = models.URLField(max_length=400)
    category = models.CharField(max_length=100)
    stores = models.CharField(max_length=100)


# Return name
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ['id']