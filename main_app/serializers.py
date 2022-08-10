from rest_framework import serializers

from .models import PoliceCalls


class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceCalls
        fields = '__all__'
