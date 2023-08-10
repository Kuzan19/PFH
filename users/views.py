from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView

from users.forms import UserRegistrationForms, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile


class UserDetailView(DetailView):
    """
    Представление для просмотра профиля
    """
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/userpage.html'
    slug_url_kwarg = 'slug_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.user.username}'
        return context


class UserUpdateView(UpdateView):
    """Представление для редактирования профиля"""

    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profedit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(UserUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_page', args=[self.slug])


class RegisterUser(SuccessMessageMixin, CreateView):

    form_class = UserRegistrationForms
    template_name = 'users/register.html'
    success_url = reverse_lazy('hub')
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')


class LoginUser(SuccessMessageMixin, LoginView):

    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class LogoutUser(LogoutView):
    """Выход с сайта"""
    next_page = '/hub'
