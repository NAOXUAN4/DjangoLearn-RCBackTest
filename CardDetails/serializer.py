from rest_framework import serializers   #导入序列化器

from CardDetails.models import CardDetailsModel


class CardDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDetailsModel
        fields = '__all__'
