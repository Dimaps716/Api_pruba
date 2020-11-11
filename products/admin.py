

# Register your models here.
from django.contrib import admin

# Register your models here.
from products import models

# administrator access to create, delete and edit articles
admin.site.register(models.items)
