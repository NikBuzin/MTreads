# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'brand'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'


class CategoryStat(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    date = models.DateTimeField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    brands = models.IntegerField(blank=True, null=True)
    sellers = models.IntegerField(blank=True, null=True)
    items = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_stat'


class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=400)
    color = models.CharField(max_length=500, blank=True, null=True)
    parameters = models.CharField(max_length=1000, blank=True, null=True)
    sizes = models.CharField(max_length=500, blank=True, null=True)
    appear_date = models.DateTimeField(blank=True, null=True)
    first_review_date = models.DateTimeField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    seller = models.ForeignKey('Seller', models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    goods = models.ForeignKey(Goods, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsStat(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods = models.ForeignKey(Goods, models.DO_NOTHING)
    date = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    discounted_price = models.IntegerField(blank=True, null=True)
    sales = models.BigIntegerField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    questions = models.IntegerField(blank=True, null=True)
    answers = models.IntegerField(blank=True, null=True)
    rating = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_stat'


class Position(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_category = models.ForeignKey(GoodsCategory, models.DO_NOTHING)
    date = models.DateTimeField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'role'


class Seller(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'seller'


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods = models.ForeignKey(Goods, models.DO_NOTHING)
    date = models.DateTimeField(blank=True, null=True)
    size = models.CharField(max_length=300, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class UserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, blank=True, null=True)
    password_hash = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'users'
