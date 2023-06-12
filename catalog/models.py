from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    descr = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.FloatField()
    reviews = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Usercart(models.Model):
    user_id = models.IntegerField()
    user_pr = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_pr_quantity = models.IntegerField()
    # user_total_price=models.FloatField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
