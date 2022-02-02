from django_filters.rest_framework import FilterSet, CharFilter

from logistic.models import Stock


class StockFilter(FilterSet):
    title = CharFilter(field_name="products__title", lookup_expr='icontains')
    description = CharFilter(field_name="products__description", lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ['products', 'title', 'description']
