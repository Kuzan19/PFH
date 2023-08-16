from django.contrib.auth import login
from django.forms import inlineformset_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView

from hub.forms import HubDoggyForm, AddDoggyFormSet
from hub.models import HubDoggyModel, PhotoDoggyModel
from users.forms import UserRegistrationForms, UserLoginForm, UserUpdateForm, ProfileUpdateForm, UserChangePasswordForm
from users.models import Profile


class UserDetailView(DetailView):
    """Представление для просмотра профиля"""

    model = Profile
    context_object_name = 'profile'
    template_name = 'users/userpage.html'
    slug_url_kwarg = 'slug_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.user.username}'
        return context


class UserUpdateView(UpdateView):
    """Представление для редактирования профиля пользователя"""

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


class AddDoggyView(CreateView):

    template_name = 'users/add_doggy.html'
    form_class = HubDoggyForm

    def get_context_data(self, **kwargs):
        context = super(AddDoggyView, self).get_context_data(**kwargs)
        context['doggy_formset'] = AddDoggyFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        doggy_formset = AddDoggyFormSet(self.request.POST, self.request.FILES)
        if form.is_valid() and doggy_formset.is_valid():
            return self.form_valid(request, form, doggy_formset)
        else:
            return self.form_invalid(request, form, doggy_formset)

    def form_valid(self, request, form, doggy_formset):
        self.object = form.save(commit=False)
        self.object.seller = request.user
        self.object.save()
        doggys = doggy_formset.save(commit=False)
        for meta in doggys:
            meta.doggy = self.object
            meta.save()
        return HttpResponseRedirect('/hub')

    def form_invalid(self, form, doggy_formset):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  doggy_formset=doggy_formset))


class EditPasswordUser(SuccessMessageMixin, PasswordChangeView):
    """Представления изменения пароля"""
    form_class = UserChangePasswordForm
    template_name = "users/user_password_change.html"
    success_message = "Пароль успешно изменен"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля на сайте'
        return context

    def get_success_url(self):
        return reverse_lazy('edit_password_page', kwargs={'slug': self.request.user.profile.slug})


class RegisterUser(SuccessMessageMixin, CreateView):
    """Представление для регистрации нового пользователя"""

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
    """Представление для авторизации пользователя"""

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
