from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAuthenticatedOrOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticatedOrOwnerOrReadOnly]

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     # if self.action in ["create", "update"]:
    #     #     return [IsAuthenticated()]
    #     # return []
