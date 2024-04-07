from django.contrib import admin
from .models import Food, ConsumptionTracker
# Register your models here.
admin.site.register(Food)

@admin.register(ConsumptionTracker)
class ConsumptionList(admin.ModelAdmin):
    list_display = ['user', 'food_consumed', 'date_created']