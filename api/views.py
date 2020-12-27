from django.http import JsonResponse
from django.shortcuts import render
from  django.db import models

from .models import GoodsCategory, Goods, GoodsStat, CategoryStat, Category, UserRole, Users, Brand, Stock, Role, Seller, Position

# Create your views here.


def index(request):
    """Информация о карточке товара"""
    goodsId = 1
    name = 'Пульсометр'
    brand = 'Филипс'
    vendor = 'ИП Оганесян'
    price = [10000, 10500, 17000, 14000, 13200, 15000, 16500]
    discountedPrice = [9800, 9500, 16000, 13000, 11000, 14000, 15500]
    discoveryDate = '11.12.2018'
    discoveryReview = '29.12.2018'
    comments = {
        'answers': [134, 148, 150, 155, 171, 171, 174],
        'questions': [144, 158, 160, 165, 181, 181, 184]
    }
    categoryPosition = [
        {'name': 'Пульсометр',
         'position': [10, 8, 6, 5, 4, 3, 2],
         'date': ['25.12.2020', '24.12.2020', '23.12.2020', '22.12.2020', '21.12.2020', '20.12.2020', '19.12.2020']
        }
    ]
    rating = [4.50, 4.21, 4.00, 4.12, 4.23, 4.36, 4.76]
    remainder = [100, 70, 40, 120, 100, 80, 140]
    sales = [0, 30, 30, 40, 20, 20, 45]
    date = ['25.12.2020', '24.12.2020', '23.12.2020', '22.12.2020', '21.12.2020', '20.12.2020', '19.12.2020',]
    revenue = [0, 130000, 150000, 120000, 100000, 1350000, 170000]
    image = ['https://www.google.com/aclk?sa=l&ai=DChcSEwj06qnn1ujtAhWXn7IKHXLIDysYABAHGgJscg&sig=AOD64_0ksGNQbAs_fexm6LPBlK5cdt6jzw&adurl&ctype=5&ved=2ahUKEwiZ8J_n1ujtAhVIxyoKHU9DDlUQwg96BAgBEDc']

    context = {
        'goodsId': goodsId,
        'name': name,
        'brand': brand,
        'vendor': vendor,
        'price': price,
        'discountedPrice': discountedPrice,
        'discoveryDate': discoveryDate,
        'discoveryReview': discoveryReview,
        'comments': comments,
        'categoryPosition': categoryPosition,
        'rating': rating,
        'remainder': remainder,
        'sales': sales,
        'date': date,
        'revenue': revenue,
        'image': image
    }

    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(context)