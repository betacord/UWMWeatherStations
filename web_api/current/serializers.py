from rest_framework import serializers

from readings.models import Reading, Station


class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('id', 'modified', 'temperature')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'name', 'lon', 'lat')
