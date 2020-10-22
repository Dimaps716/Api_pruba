
"""items Api view"""


from products.models import items
from rest_framework.decorators import api_view
from rest_framework.response import Response


#  create your views here.
from products.serializers import itemsSerializer

# list all products
@api_view(['GET'])
def itemsList(request):
    item = items.objects.all()
    serializer = itemsSerializer(item, many=True)
    return Response(serializer.data)
