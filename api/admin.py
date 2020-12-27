from django.contrib import admin
from .models import Goods, GoodsCategory, GoodsStat, Category, CategoryStat, Seller, Stock, Position, UserRole,Users, Role, Brand
# Register your models here.
admin.site.register(GoodsStat)
admin.site.register(Goods)
admin.site.register(GoodsCategory)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Position)
admin.site.register(Stock)
admin.site.register(Users)
admin.site.register(UserRole)
admin.site.register(CategoryStat)
admin.site.register(Seller)
admin.site.register(Role)
