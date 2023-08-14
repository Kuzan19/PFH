from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


from .models import HubDoggyModel


class HomePageView(View):
    """Домашняя страница/открывашка"""

    def get(self, request):
        return render(request, 'hub/basepage.html')

    def post(self, request):
        pass


class SomeDoggyPage(View):
    """Страница определенного объявления"""
    def get(self, request, slug_doggy: str, id_doggy: int):
        doggy = get_object_or_404(HubDoggyModel, slug=slug_doggy, id=id_doggy)
        return render(request, "hub/doggypage.html", context={'doggy': doggy})

    def post(self, request):
        pass


class HubPageView(ListView):
    """Главная страница с объявлениями"""

    doggyes = HubDoggyModel.objects.all()
    for doggy in doggyes:
        doggy.save()

    model = HubDoggyModel
    template_name = 'hub/hubpage.html'
    context_object_name = 'pets'
