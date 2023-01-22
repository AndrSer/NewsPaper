from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter, ModelChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    date_posting_after = DateTimeFilter(
        field_name='date_posting',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )

    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'kind': ['exact']
        }
