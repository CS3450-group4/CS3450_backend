from django.db import models


class UserInfo(models.Model):
    authLevel = models.JSONField(default=dict)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    actingLevel = models.PositiveSmallIntegerField()
    hoursWorked = models.PositiveIntegerField(default=0)


class MenuItem(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField(default=2)
    ingredientList = models.JSONField(default=dict)


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
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "auth.User", related_name="orders", on_delete=models.CASCADE
    )
    # TODO: set choices on orderStatus
    orderStatus = models.CharField(max_length=200, default="unfullfilled")
    ingredientList = models.JSONField(default=dict)

    class Meta:
        ordering = ["created"]
