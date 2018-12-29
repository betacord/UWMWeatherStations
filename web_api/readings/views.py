from rest_framework import viewsets
from readings.models import Reading
from readings.serializers import ReadingSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by('-modified')
    serializer_class = ReadingSerializer
