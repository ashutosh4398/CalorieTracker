from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, View

from .models import ConsumptionTracker, Food

# Create your views here.


class FoodList(View):
    template_name = "food/index.html"
    queryset = Food.objects.all()

    def get_context_data(self, **kwargs: Any):
        context = {}
        context.update({"foods": self.queryset})
        consumed_food = ConsumptionTracker.objects.select_related(
            "food_consumed"
        ).filter(user=self.request.user)

        context.update({"foods_consumed": consumed_food})
        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        food_consumed = request.POST.getlist("food_ids")
        objs = [
            ConsumptionTracker(food_consumed_id=food_id, user=request.user)
            for food_id in food_consumed
        ]
        resp = ConsumptionTracker.objects.bulk_create(objs)
        return redirect("index")

def delete_track(request, pk):
    if request.method != "POST":
        return redirect("index")
    history = ConsumptionTracker.objects.get(id=pk)
    history.delete()
    return redirect("index")
