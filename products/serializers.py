from rest_framework import serializers
from products.models import items


class itemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = items
        # fields = ('id',
        # 'name',
        # 'picture_url',
        # 'url_located',
        # 'category',
        # store
        # )
        fields = '__all__'