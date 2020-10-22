# Create your views here.
"""api  URLs."""

# django
from django.urls import path

# views

from products import views

urlpatterns = [
    # url de las recetas 
    path(
        route='api/items-list/',
        view= views.itemsList,
        name= 'items_list'
    ),
]