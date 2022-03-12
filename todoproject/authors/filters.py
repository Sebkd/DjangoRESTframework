from django_filters import rest_framework as filters
from .models import Author


class AuthorFilter(filters.FilterSet):
    # username = filters.CharFilter(lookup_expr='contains')
    # username = filters.ChoiceFilter('username')
    username = filters.AllValuesFilter()

    class Meta:
        model = Author
        fields = ['username']
