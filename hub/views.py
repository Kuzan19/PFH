from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import get_object_or_404

from .forms import PhotoDoggyForm
from .models import HubDoggyModel


class HomePageView(View):
    """Домашняя страница/открывашка"""

    def get(self, request):
        return render(request, 'hub/basepage.html')

    def post(self, request):
        pass


class SomeDoggyPage(UpdateView):
    """Страница определенного объявления"""

    model = HubDoggyModel
    form_class = PhotoDoggyForm
    context_object_name = 'doggy'
    template_name = "hub/doggypage.html"
    slug_url_kwarg = 'slug_doggy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Подробная информация: {self.object.name}'
        context['form'] = PhotoDoggyForm()
        return context

    def post(self, request, slug_doggy):
        form = PhotoDoggyForm(request.POST, request.FILES)
        dog = HubDoggyModel.objects.get(slug=slug_doggy)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.doggy_id = dog.id
            instances.save()
        return render(request, "hub/doggypage.html", context={'form': form})


class HubPageView(ListView):
    """Главная страница с объявлениями"""

    model = HubDoggyModel
    template_name = 'hub/hubpage.html'
    context_object_name = 'pets'
    paginate_by = 3



