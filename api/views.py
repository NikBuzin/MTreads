from django.http import JsonResponse
from django.shortcuts import render
from django.db import models, connection
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict

from .models import GoodsCategory, Goods, GoodsStat, CategoryStat, Category, UserRole, Users, Brand, Stock, Role, Seller, Position

import json, time
# Create your views here.

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

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


@csrf_exempt
def test_get_id(request):
    start = time.time()
    limit = 7
    body = json.loads(request.body.decode('utf-8'))
    goodsId = body.get('goodsId')
    cursor = connection.cursor();
    cursor.execute('''
    SELECT
            cur_goods.date,
            cur_goods.sales,
            cur_goods.discounted_price,
            cur_stock.remainder
        FROM (
        	SELECT
                DISTINCT ON (date) date::date,
                sales,
                discounted_price
            FROM goods_stat
        	WHERE goods_id = %s
        	ORDER BY date DESC
            LIMIT %s
        	) AS cur_goods
        inner JOIN (
			SELECT
				DISTINCT ON (date::date) date::date,
				stocks.remainder
			FROM (
				SELECT
					date,
					sum(quantity) as remainder
				FROM stock
				WHERE goods_id = %s
				GROUP BY date
			) AS stocks
        	) AS cur_stock
        ON cur_goods.date = cur_stock.date::date
        ORDER BY date DESC
    ''', [goodsId, limit, goodsId])

    data = dictfetchall(cursor)

    context = {
        'list': data,
    }

    print(time.time() - start)
    return JsonResponse(OrderedDict(context))


@csrf_exempt
def goods_lite(request):
    ### Метод получения данных для лайт версии карточки товара(расширение). ###
    start = time.time()

    body = json.loads(request.body.decode('utf-8'))
    goodsId = body.get('goodsId')
    limit = body.get('period')

    if limit == None:
        limit = 31

    cursor = connection.cursor();

    cursor.execute('''
        SELECT
            cur_goods.date,
            cur_goods.sales,
            cur_goods.discounted_price,
            cur_stock.remainder
        FROM (
        	SELECT
                DISTINCT ON (date) date::date,
                sales,
                discounted_price
            FROM goods_stat
        	WHERE goods_id = %s
        	ORDER BY date DESC
            LIMIT %s
        	) AS cur_goods
        LEFT JOIN (
			SELECT
				DISTINCT ON (date::date) date::date,
				stocks.remainder
			FROM (
				SELECT
					date,
					sum(quantity) as remainder
				FROM stock
				WHERE goods_id = %s
				GROUP BY date
			) AS stocks
        	) AS cur_stock
        ON cur_goods.date = cur_stock.date::date
        ORDER BY date DESC
    ''', [goodsId, limit, goodsId])

    """data = dictfetchall(cursor)"""

    test_data = get_all(cursor)
    if len(test_data)>0:
        context = {
            'list': test_data,
        }
    else:
        log = []
        with open('Goods_not_found.txt') as f:
            for line in f:
                log.append([int(x) for x in line.split()])
        f.close()
        if [goodsId] not in log:
            f = open('Goods_not_found.txt', 'a')
            f.write(str(goodsId) + '\n')
            f.close()
        context = {
            'list': 'Error: goods not found',
        }

    print(time.time() - start)
    return JsonResponse(OrderedDict(context))


def get_all(cursor):
    data = cursor.fetchall()
    result = []
    array_sales = []
    avg_sales = []
    remainder = []
    discount_price = []
    avg_sales_count = 0
    desc = cursor.description

    for day in range(0, len(data)):
        discount_price.append(data[day][2])

    for day in range(0, len(data)):
        remainder.append(data[day][3])

    remainder = avg_array(remainder)
    discount_price = avg_array(discount_price)

    for day in range(0,len(data)):
        if day !=len(data)-1:
            array_sales.append(-1*get_sales(remainder[day], remainder[day+1]))
            if array_sales[day] >= 0:
                avg_sales.append(array_sales[day])

    array_sales = avg_array(array_sales)

    for day in range(len(array_sales)):
        result.append(
            {
                desc[0][0]: data[day][0],
                desc[1][0]: abs(array_sales[day]),
                desc[2][0]: discount_price[day],
                desc[3][0]: remainder[day]
            }
        )
    return result


'''Усреднение значений массива'''


def avg_array(array):
    mean_array = mean(array)
    for day in range(0, len(array)):
        if type(array[day])!= int:
            array[day] = 0
        if int(array[day]) > mean_array+mean_array*0.95 or int(array[day]) < mean_array - mean_array*0.95:
            change_array(array, day)
    return array


'''Удаление из массива значения с сохранением размерности и вставкой на то место среднего'''


def change_array(array, day):
    temp_array = array.copy()
    temp_array.pop(day)
    array[day] = mean(temp_array)
    return array


'''Вычисление среднего значения в массиве'''


def mean(array):
    mean_result = 0
    for i in range(0,len(array)):
        if type(array[i]) == int:
            mean_result+=array[i]
    mean_result/=len(array)
    return int(mean_result)


'''Получание количества продаж на основе остатков на складе'''


def get_sales(old_rem, now_rem):
    if type(old_rem) == int and type(now_rem) == int:
        sales = old_rem - now_rem
    else: sales = 0
    return sales


@csrf_exempt
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

@csrf_exempt
def category_all(request):
    ### Метод получения полного списка категорий по parent_id. ###
    start = time.time()

    cursor = connection.cursor();
    cursor.execute('''
        SELECT *
        FROM category
        WHERE parent_id IS NULL
    ''')

    data = dictfetchall(cursor)

    context = {
        'list': data,
    }

    print(time.time() - start)
    return JsonResponse(OrderedDict(context))

@csrf_exempt
def category_path(request):
    ### Метод получения пути для категории. ###
    start = time.time()

    body = json.loads(request.body.decode('utf-8'))
    category_id = body.get('category_id')

    context = {}

    cursor = connection.cursor();
    cursor.execute('''
        WITH RECURSIVE r AS (
            SELECT *
            	FROM category
            	WHERE id = %s
            UNION
            SELECT category.*
            	FROM r, category
            	WHERE category.id = r.parent_id
        )
        SELECT * FROM r;
    ''', [category_id])
    context['list'] = dictfetchall(cursor)

    cursor.execute('''
        SELECT *
        FROM category
        WHERE parent_id = %s
    ''', [category_id])
    context['childs'] = dictfetchall(cursor)

    print(time.time() - start)
    return JsonResponse(OrderedDict(context))
