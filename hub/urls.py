from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('hub', views.HubPageView.as_view(), name="hub_page"),
    path('hub/<slug:slug_doggy>', views.SomeDoggyPage.as_view(), name="doggy_page"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
