"""items"""
# Django
from django.db import models

# creation of the database model its fields and parameters
class items(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    picture_url = models.URLField(max_length=200)
    url_located = models.URLField(max_length=200)
    category = models.CharField(max_length=80)
    publication_date= models.CharField(max_length=50)
    ranting= models.IntegerField()
    comments= models.TextField(max_length=500)
    description = models.TextField(max_length=300)
    stores = models.CharField(max_length=80)


# Return name
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ['id']