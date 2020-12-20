import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
        start_date = DateFilter(field_name="date_created", lookup_expr = 'gte')# 2nd here we customise
        end_date = DateFilter(field_name="date_created", lookup_expr = 'lte')
        note= CharFilter(field_name='note', lookup_expr='icontains')       
        class Meta:
                model = Order
                fields = '__all__'
                exclude = ['customer', 'date_created']
                # here is to exclude some field in Order class
                # 1st we exclude these 2 fields because we want to customise it
        