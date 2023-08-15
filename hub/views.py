from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


from .models import HubDoggyModel


class HomePageView(View):
    """Домашняя страница/открывашка"""

    def get(self, request):
        return render(request, 'hub/basepage.html')

    def post(self, request):
        pass


    # def get(self, request, slug_doggy: str, id_doggy: int):
    #     doggy = get_object_or_404(HubDoggyModel, slug=slug_doggy, id=id_doggy)
    #     return render(request, "hub/doggypage.html", context={'doggy': doggy})


class SomeDoggyPage(DetailView):
    """Страница определенного объявления"""

    model = HubDoggyModel
    context_object_name = 'doggy'
    template_name = "hub/doggypage.html"
    slug_url_kwarg = 'slug_doggy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Подробная информация: {self.object.name}'
        return context


class HubPageView(ListView):
    """Главная страница с объявлениями"""

    model = HubDoggyModel
    template_name = 'hub/hubpage.html'
    context_object_name = 'pets'
