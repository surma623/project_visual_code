from django.urls import path

from .views import view_shop_index, view_groups_list, view_products_list

app_name = 'shopapp'

urlpatterns = [
    path('', view_shop_index, name='index'),
    path('groups/', view_groups_list, name='groups_list'),
    path('products/', view_products_list, name='products_list'),
]