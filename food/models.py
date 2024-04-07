from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)

    carbs = models.FloatField()  # in grams
    proteins = models.FloatField()  # in grams
    fats = models.FloatField()  # in grams

    calories = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class ConsumptionTracker(models.Model):
    food_consumed = models.ForeignKey("food.Food", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)
