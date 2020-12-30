from django.http import JsonResponse
from django.shortcuts import render
from  django.db import models

from .models import GoodsCategory, Goods, GoodsStat, CategoryStat, Category, UserRole, Users, Brand, Stock, Role, Seller, Position

# Create your views here.


def goods_cart(request):
    """Информация о карточке товара"""
    name = 'Пульсометр'
    brand = 'Филипс'
    vendor = 'ИП Оганесян'
    date = {
        '25.12.2020': {
            'revenue': 200000,
            'sales': 72,
            'remainder': 120,
            'price': 12000,
            'discountedPrice': 11000,
            'rating': 4.55,
            'comments': {
                'answers': 180,
                'questions': 190,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 9,
                 },
                {
                    'name': 'Электроника',
                    'position': 7,
                },
            ],

        },
        '24.12.2020': {
            'revenue': 170000,
            'sales': 70,
            'remainder': 140,
            'price': 13000,
            'discountedPrice': 12500,
            'rating': 4.59,
            'comments': {
                'answers': 168,
                'questions': 170,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 11,
                },
                {
                    'name': 'Электроника',
                    'position': 10,
                },
            ],

        },
        '23.12.2020': {
            'revenue': 170000,
            'sales': 65,
            'remainder': 80,
            'price': 10000,
            'discountedPrice': 10000,
            'rating': 4.70,
            'comments': {
                'answers': 160,
                'questions': 165,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 7,
                },
                {
                    'name': 'Электроника',
                    'position': 7,
                },
            ],

        },
        '22.12.2020': {
            'revenue': 170000,
            'sales': 60,
            'remainder': 70,
            'price': 11000,
            'discountedPrice': 10500,
            'rating': 4.85,
            'comments': {
                'answers': 158,
                'questions': 168,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 5,
                },
                {
                    'name': 'Электроника',
                    'position': 6,
                },
            ],

        },
        '21.12.2020': {
            'revenue': 170000,
            'sales': 57,
            'remainder': 100,
            'price': 11500,
            'discountedPrice': 11500,
            'rating': 4.49,
            'comments': {
                'answers': 144,
                'questions': 154,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 4,
                },
                {
                    'name': 'Электроника',
                    'position': 12,
                },
            ],

        },
        '20.12.2020': {
            'revenue': 170000,
            'sales': 52,
            'remainder': 140,
            'price': 11000,
            'discountedPrice': 10000,
            'rating': 4.74,
            'comments': {
                'answers': 144,
                'questions': 154,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 8,
                },
                {
                    'name': 'Электроника',
                    'position': 8,
                },
            ],

        },
        '19.12.2020': {
            'revenue': 170000,
            'sales': 45,
            'remainder': 140,
            'price': 10000,
            'discountedPrice': 9800,
            'rating': 4.50,
            'comments': {
                'answers': 134,
                'questions': 144,
            },
            'categoryPosition': [
                {
                    'name': 'Пульсометр',
                    'position': 10,
                 },
                {
                    'name': 'Электроника',
                    'position': 8,
                },
            ],

        },
    }
    discoveryDate = '11.12.2018'
    discoveryReview = '29.12.2018'
    image = ['https://www.google.com/aclk?sa=l&ai=DChcSEwj06qnn1ujtAhWXn7IKHXLIDysYABAHGgJscg&sig=AOD64_0ksGNQbAs_fexm6LPBlK5cdt6jzw&adurl&ctype=5&ved=2ahUKEwiZ8J_n1ujtAhVIxyoKHU9DDlUQwg96BAgBEDc']

    context = {
        'name': name,
        'brand': brand,
        'vendor': vendor,
        'discoveryDate': discoveryDate,
        'discoveryReview': discoveryReview,
        'date': date,
        'image': image
    }

    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(context)


def goods_lite(request):
    """Метод получения данных для лайт версии карточки товара(расширение)."""
    date = {
        '25.12.2020': {
            'revenue': 0,
            'sales': 0,
            'remainder': 100
        },
        '24.12.2020': {
            'revenue': 130000,
            'sales': 30,
            'remainder': 70
        },
        '23.12.2020': {
            'revenue': 150000,
            'sales': 30,
            'remainder': 40
        },
        '22.12.2020': {
            'revenue': 120000,
            'sales': 40,
            'remainder': 120
        },
        '21.12.2020': {
            'revenue': 100000,
            'sales': 20,
            'remainder': 100
        },
        '20.12.2020': {
            'revenue': 135000,
            'sales': 20,
            'remainder': 80
        },
        '19.12.2020': {
            'revenue': 170000,
            'sales': 45,
            'remainder': 140
        },
    }
    context = {
        'date': date,
    }
    return JsonResponse(context)


def goods_list(request):
    """Информация о нескольких карточках товара"""
    goods = {
        '12675': {
            'name': 'Пульсометр',
            'brand': 'Филипс',
            'vendor': 'ИП Оганесян',
            'date': {
                '25.12.2020': {
                    'revenue': 200000,
                    'sales': 72,
                    'remainder': 120,
                    'price': 12000,
                    'discountedPrice': 11000,
                    'rating': 4.55,
                    'comments': {
                        'answers': 180,
                        'questions': 190,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 9,
                        },
                        {
                            'name': 'Электроника',
                            'position': 7,
                        },
                    ],
                },
                '24.12.2020': {
                    'revenue': 170000,
                    'sales': 70,
                    'remainder': 140,
                    'price': 13000,
                    'discountedPrice': 12500,
                    'rating': 4.59,
                    'comments': {
                        'answers': 168,
                        'questions': 170,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 11,
                        },
                        {
                            'name': 'Электроника',
                            'position': 10,
                        },
                    ],
                },
                '23.12.2020': {
                    'revenue': 170000,
                    'sales': 65,
                    'remainder': 80,
                    'price': 10000,
                    'discountedPrice': 10000,
                    'rating': 4.70,
                    'comments': {
                        'answers': 160,
                        'questions': 165,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 7,
                        },
                        {
                            'name': 'Электроника',
                            'position': 7,
                        },
                    ],
                },
                '22.12.2020': {
                    'revenue': 170000,
                    'sales': 60,
                    'remainder': 70,
                    'price': 11000,
                    'discountedPrice': 10500,
                    'rating': 4.85,
                    'comments': {
                        'answers': 158,
                        'questions': 168,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 5,
                        },
                        {
                            'name': 'Электроника',
                            'position': 6,
                        },
                    ],
                },
                '21.12.2020': {
                    'revenue': 170000,
                    'sales': 57,
                    'remainder': 100,
                    'price': 11500,
                    'discountedPrice': 11500,
                    'rating': 4.49,
                    'comments': {
                        'answers': 144,
                        'questions': 154,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 4,
                        },
                        {
                            'name': 'Электроника',
                            'position': 12,
                        },
                    ],
                },
                '20.12.2020': {
                    'revenue': 170000,
                    'sales': 52,
                    'remainder': 140,
                    'price': 11000,
                    'discountedPrice': 10000,
                    'rating': 4.74,
                    'comments': {
                        'answers': 144,
                        'questions': 154,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 8,
                        },
                        {
                            'name': 'Электроника',
                            'position': 8,
                        },
                    ],
                },
                '19.12.2020': {
                    'revenue': 170000,
                    'sales': 45,
                    'remainder': 140,
                    'price': 10000,
                    'discountedPrice': 9800,
                    'rating': 4.50,
                    'comments': {
                        'answers': 134,
                        'questions': 144,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 10,
                        },
                        {
                            'name': 'Электроника',
                            'position': 8,
                        },
                    ],

                },
            },
            'discoveryDate': '11.12.2018',
            'discoveryReview': '29.12.2018',
            'image': [
                'https://www.google.com/aclk?sa=l&ai=DChcSEwj06qnn1ujtAhWXn7IKHXLIDysYABAHGgJscg&sig'
                '=AOD64_0ksGNQbAs_fexm6LPBlK5cdt6jzw&adurl&ctype=5&ved=2ahUKEwiZ8J_n1ujtAhVIxyoKHU9DDlUQwg96BAgBEDc']
        },
        '12644': {
            'name': 'Пульсометр',
            'brand': 'Филипс',
            'vendor': 'ИП Оганесян',
            'date': {
                '25.12.2020': {
                    'revenue': 200000,
                    'sales': 72,
                    'remainder': 120,
                    'price': 12000,
                    'discountedPrice': 11000,
                    'rating': 4.55,
                    'comments': {
                        'answers': 180,
                        'questions': 190,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 9,
                        },
                        {
                            'name': 'Электроника',
                            'position': 7,
                        },
                    ],
                },
                '24.12.2020': {
                    'revenue': 170000,
                    'sales': 70,
                    'remainder': 140,
                    'price': 13000,
                    'discountedPrice': 12500,
                    'rating': 4.59,
                    'comments': {
                        'answers': 168,
                        'questions': 170,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 11,
                        },
                        {
                            'name': 'Электроника',
                            'position': 10,
                        },
                    ],
                },
                '23.12.2020': {
                    'revenue': 170000,
                    'sales': 65,
                    'remainder': 80,
                    'price': 10000,
                    'discountedPrice': 10000,
                    'rating': 4.70,
                    'comments': {
                        'answers': 160,
                        'questions': 165,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 7,
                        },
                        {
                            'name': 'Электроника',
                            'position': 7,
                        },
                    ],
                },
                '22.12.2020': {
                    'revenue': 170000,
                    'sales': 60,
                    'remainder': 70,
                    'price': 11000,
                    'discountedPrice': 10500,
                    'rating': 4.85,
                    'comments': {
                        'answers': 158,
                        'questions': 168,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 5,
                        },
                        {
                            'name': 'Электроника',
                            'position': 6,
                        },
                    ],
                },
                '21.12.2020': {
                    'revenue': 170000,
                    'sales': 57,
                    'remainder': 100,
                    'price': 11500,
                    'discountedPrice': 11500,
                    'rating': 4.49,
                    'comments': {
                        'answers': 144,
                        'questions': 154,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 4,
                        },
                        {
                            'name': 'Электроника',
                            'position': 12,
                        },
                    ],
                },
                '20.12.2020': {
                    'revenue': 170000,
                    'sales': 52,
                    'remainder': 140,
                    'price': 11000,
                    'discountedPrice': 10000,
                    'rating': 4.74,
                    'comments': {
                        'answers': 144,
                        'questions': 154,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 8,
                        },
                        {
                            'name': 'Электроника',
                            'position': 8,
                        },
                    ],
                },
                '19.12.2020': {
                    'revenue': 170000,
                    'sales': 45,
                    'remainder': 140,
                    'price': 10000,
                    'discountedPrice': 9800,
                    'rating': 4.50,
                    'comments': {
                        'answers': 134,
                        'questions': 144,
                    },
                    'categoryPosition': [
                        {
                            'name': 'Пульсометр',
                            'position': 10,
                        },
                        {
                            'name': 'Электроника',
                            'position': 8,
                        },
                    ],

                },
            },
            'discoveryDate': '11.12.2018',
            'discoveryReview': '29.12.2018',
            'image': [
                'https://www.google.com/aclk?sa=l&ai=DChcSEwj06qnn1ujtAhWXn7IKHXLIDysYABAHGgJscg&sig'
                '=AOD64_0ksGNQbAs_fexm6LPBlK5cdt6jzw&adurl&ctype=5&ved=2ahUKEwiZ8J_n1ujtAhVIxyoKHU9DDlUQwg96BAgBEDc']
        }
    }

    context = {
        'goods': goods,
    }

    # Render the HTML template index.html with the data in the context variable
    return JsonResponse(context)

