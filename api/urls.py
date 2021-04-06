from django.urls import path
from . import views

urlpatterns = [
    path('goods/', views.goods_cart, name='goods_cart'),
    path('goods-lite/', views.goods_lite, name='goods_lite'),
    path('goods-list/', views.goods_list, name='goods_list'),
    path('category-all/', views.category_all, name='category_all'),
    path('category-path/', views.category_path, name='category_path'),
    path('test/', views.test_get_id, name = 'test_get_id'),
]
