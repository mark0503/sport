import django_filters
from .models import Anketa


class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Anketa
        fields = ['types', 'price', 'age', 'sity']