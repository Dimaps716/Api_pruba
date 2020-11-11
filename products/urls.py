# Create your views here.
"""api  URLs."""

# django
from django.urls import path

# views
from products import views

urlpatterns = [
    # url of the items
    path(
        route='api/items-list/',
        view= views.itemsList,
        name= 'items_list'
    ),
    path(
        route='api/items-datail/<str:pk>/',
        view= views.itemsDetail,
        name= 'items_datail'
    ),
    path(
        route='api/items-create/',
        view= views.itemsCreate,
        name= 'items_create'
    ),
    path(
        route='api/items-update/<str:pk>/',
        view= views.itemsUpdate,
        name= 'items_update'
    ),
    path(
        route='api/items-delete/<str:pk>/',
        view= views.itemsDelete,
        name= 'items_delete'
    ),
]
