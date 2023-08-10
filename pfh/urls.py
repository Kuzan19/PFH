from django.contrib import admin
from django.urls import path, include
from rest_api.views import HubAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hub.urls')),
    path('user/', include('users.urls')),

    # REST Urls
    path('api/v1/hubdoggy', HubAPIView.as_view()),
]
