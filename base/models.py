from django.db import models


class User(models.Model):
    def __str__(self):
        return self.userName
    authLevel = models.PositiveSmallIntegerField()
    # TODO: look into hashing passwords
    password = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    balance = models.IntegerField()
    actingLevel = models.PositiveSmallIntegerField()
    hoursWorked = models.PositiveIntegerField()


class MenuItem(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField(default=2)
    ingredients_list = models.JSONField(default=dict)


class Ingredient(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    retailCost = models.PositiveIntegerField()
    wholeSaleCost = models.PositiveIntegerField()
    isMilk = models.BooleanField()
    options = models.IntegerField(default=0)


class Order(models.Model):
    price = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderStatus = models.CharField(max_length=200)
    ingredients_list = models.JSONField(default=dict)

