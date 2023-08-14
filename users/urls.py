from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name="register_page"),
    path('login', views.LoginUser.as_view(), name="login_page"),
    path('logout', views.LogoutUser.as_view(), name="logout_page"),
    path('<slug:slug_profile>', views.UserDetailView.as_view(), name="profile_page"),
    path('edit_profile/', views.UserUpdateView.as_view(), name="edit_page"),
    path('add_doggy/', views.AddDoggyView.as_view(), name="add_doggy_page")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

