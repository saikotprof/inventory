from django.db import models


class Brand(models.Model):
    company_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.company_name


class Mobile(models.Model):
    name = models.CharField(max_length=40)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()

    choose = [
        ('Available', 'Item is ready to be purchased'),
        ('Sold', 'Item is already purchased'),
        ('Sold Out', 'Item is comming soon'),
    ]

    status = models.CharField(max_length=40, choices=choose, default='Sold')
    issues = models.CharField(max_length=40, default='No Issues')

    def __str__(self):
        return f"{self.name} - {self.brand} - {self.price}"


class Apple(Mobile):
    pass


class Samsung(Mobile):
    pass


class Xiaomi(Mobile):
    pass
