from rest_framework import serializers
from .models import usermodel

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = usermodel
        #exclude = ('fromm', 'to', 'message', 'hexx')
        depth = 4
        fields = '__all__'