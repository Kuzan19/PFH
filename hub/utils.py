from django.views import View
from .models import HubDoggyModel


class ContextMixin(View):
    def get_context_data(self, **kwargs):
        context = kwargs
        return context
