from datetime import datetime
from django.http import HttpResponseNotAllowed
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from readings.models import Reading
from readings.serializers import ReadingSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Reading.objects.all()

    def create(self, request, *args, **kwargs):
        reading = Reading.objects.create(
            station_id=request.user.station.id,
            temperature=request.data['temp']
            humidity=request.data['hum']
        )
        serializer = ReadingSerializer(reading)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        reading = self.get_object()

        if request.user.station.id == reading.station.id:
            reading.temperature = request.data['temp']
            reading.humidity = request.data['hum']
            reading.modified = datetime.now()
            reading.save()

            serializer = ReadingSerializer(reading, many=False)

            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('')
