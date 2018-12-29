from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from current.serializers import CurrentSerializer, StationSerializer
from readings.models import Reading, Station


class CurrentViewSet(viewsets.ModelViewSet):
    serializer_class = CurrentSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        station = self.request.query_params.get('station', None)

        if station:
            readings = Reading.objects.filter(station_id=station)
        else:
            readings = Reading.objects.all()

        return readings


class StationViewSet(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Station.objects.all()
