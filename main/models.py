from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='animals/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image_preview = models.ImageField(upload_to='products/')
    animal = models.ManyToManyField('Animal')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE)
    sales = models.ForeignKey('Sales', on_delete=models.SET_NULL, null=True, blank=True)
    top_product = models.PositiveIntegerField(default=0) #счетчик покупок товара

    def __str__(self):
        return self.name

class CategoryProduct(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Sales(models.Model):
    sales_name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    image = models.ImageField(upload_to='animals/')
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.sales_name


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.product


class Brand(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name


class ProductCount(models.Model):
    '''количество и фасовка'''
    CHOICES = {
        'шт': 'шт',# первое значение хранится в базе, второе отображается пользователю
        'кг': 'кг',
        'n': 'n',
    }
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.FloatField()
    unit = models.CharField(max_length=250, choices=CHOICES)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    description = models.TextField()
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    read_time = models.CharField(max_length=90)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):

    owner = models.CharField(max_length=50)
    description = models.TextField()
    email = models.CharField(max_length=50)
    pet = models.CharField(max_length=50)

    def __str__(self):
        return self.title



    #@property #декоратор
    #def discounted_price(self):
    #    return round(float(self.price) * 0.9, 2)  # для товаров со скидкой 10%

    # @property
    # def discounted_price(self):
    #     return self.price * (1 - self.discount / 100) # для товаров с любой скидкой

