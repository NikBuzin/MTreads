
# Create your models here.
from django.db import models
from django.urls import reverse

class Brand(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=100)

    """Возвращает название бренда"""
    def __str__(self):
        return self.name

    """Возвращает url с детальной информацией о бренде"""
    def get_absolute_url(self):
        return reverse('brand-detail', args=[str(self.id), str(self.name)])

    class Meta:
        managed = False
        db_table = 'brand'


class Category(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)

    """Возвращает название категории"""
    def __str__(self):
        return self.name

    """Возвращает url с детальной информацией о категории"""
    def get_absolute_url(self):
        return reversed('category-detail', args=[str(self.id), str(self.name), self(self.parent)])

    class Meta:
        managed = False
        db_table = 'category'


class CategoryStat(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date = models.TextField(blank=True, null=True)  # This field type is a guess.
    revenue = models.BigIntegerField(blank=True, null=True)
    brands = models.IntegerField(blank=True, null=True)
    sellers = models.IntegerField(blank=True, null=True)
    items = models.IntegerField(blank=True, null=True)

    """Возвращает название бренда"""
    def __str__(self):
        return str(self.id)

    """Возвращает url с детальной информацией о бренде"""
    def get_absolute_url(self):
        return reversed('brand-detail', args=[str(self.id)])

    class Meta:
        managed = False
        db_table = 'category_stat'


class Goods(models.Model):
    id = models.TextField(primary_key=True)
    image = models.CharField(blank=True, null=True, max_length=1000)
    name = models.CharField(max_length=400)
    color = models.CharField(blank=True, null=True, max_length=500)
    parameters = models.CharField(blank=True, null=True, max_length=1000)
    sizes = models.CharField(blank=True, null=True, max_length=500)
    appear_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    first_review_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey('Seller', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsCategory(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsStat(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    date = models.TextField(blank=True, null=True)  # This field type is a guess.
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
    id = models.TextField(primary_key=True)  # This field type is a guess.
    goods_category = models.ForeignKey(GoodsCategory, on_delete=models.DO_NOTHING)
    date = models.TextField(blank=True, null=True)  # This field type is a guess.
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class Role(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(unique=True, blank=True, null=True, max_length=50)
    description = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'role'


class Seller(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'seller'


class Stock(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    date = models.TextField(blank=True, null=True)  # This field type is a guess.
    size = models.CharField(blank=True, null=True, max_length=300)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class UserRole(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    user = models.ForeignKey('Users', on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'


class Users(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=100)
    email = models.CharField(blank=True, null=True, max_length=200)
    password_hash = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'users'