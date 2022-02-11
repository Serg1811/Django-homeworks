from django.db.models import Q
from django.contrib.auth.models import AnonymousUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAuthenticatedOrOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer, FavouritesSerializer


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

    def get_queryset(self):
        queryset = super(AdvertisementViewSet, self).get_queryset()
        user = self.request.user
        if isinstance(user, AnonymousUser):
            return queryset.exclude(status='DRAFT')
        if user.is_staff:
            return queryset
        return queryset.exclude(Q(status='DRAFT') & ~Q(creator=user))

    @action(detail=True, methods=['post'])
    def favourites(self, request, pk=None):
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({'status': 'Для данного действия необходимо идентифицироваться'})
        serializer = FavouritesSerializer(data={'user': user.id, 'advertisement': pk})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Добавлено в избранное'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, url_path='favourites', url_name='favourites')
    def list_favourites(self, request):
        user = request.user
        if isinstance(user, AnonymousUser):
            return Response({'status': 'Для данного действия необходимо идентифицироваться'})
        advertisements = super(AdvertisementViewSet, self).get_queryset().\
            prefetch_related('users').filter(favourites__user=user.id)
        serializer = self.get_serializer(advertisements, many=True)
        return Response(serializer.data)

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     # if self.action in ["create", "update"]:
    #     #     return [IsAuthenticated()]
    #     # return []
