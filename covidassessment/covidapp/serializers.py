from rest_framework import serializers

from .models import Covid

class CovidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Covid
        fields = ('name', 'reportedCases')