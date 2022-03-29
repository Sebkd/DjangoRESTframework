from django_filters import rest_framework as filters
from .models import Author, Book


class AuthorFilter(filters.FilterSet):
    # username = filters.CharFilter(lookup_expr='contains')
    # username = filters.ChoiceFilter('username')
    username = filters.AllValuesFilter()

    class Meta:
        model = Author
        fields = ['username']

class BookFilter(filters.FilterSet):
    authors = filters.AllValuesFilter()
    name = filters.AllValuesFilter()


    class Meta:
        model = Book
        fields = ['name', 'authors',]
