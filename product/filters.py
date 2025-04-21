import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    pricefrom = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    priceto = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    cat = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    sub_cat = django_filters.CharFilter(field_name='subcategory__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = [
            "cat",
            "sub_cat",
            "pricefrom",
            "priceto"
        ]