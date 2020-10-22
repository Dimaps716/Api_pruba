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
        # 'publication_date',
        # 'ranti',
        # 'comments',
        # 'description'
        # )
        fields = '__all__'