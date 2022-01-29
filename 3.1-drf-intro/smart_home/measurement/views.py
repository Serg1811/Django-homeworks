# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorIdView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


