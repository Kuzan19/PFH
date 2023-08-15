from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User

from users.models import Profile


class UserRegistrationForms(UserCreationForm):
    """Переопределенная форма регистрации пользователей"""

    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             "placeholder": 'Create your login', }))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  "placeholder": 'Create your login', }))
    password2 = forms.CharField(label='Please repeat password',
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  "placeholder": 'Create your login', }))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                         "placeholder": 'Create your login', }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        """Проверка email на уникальность"""

        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email


class UserLoginForm(AuthenticationForm):
    """Форма авторизации на сайте"""

    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             "placeholder": 'Create your login', }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 "placeholder": 'Create your login', }))


class UserUpdateForm(forms.ModelForm):
    """Форма обновления данных пользователя"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы под bootstrap"""

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_email(self):
        """Проверка email на уникальность"""

        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным')
        return email


class ProfileUpdateForm(forms.ModelForm):
    """Форма обновления данных профиля"""

    class Meta:
        model = Profile
        fields = ('slug', 'avatar')

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы обновления"""

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserChangePasswordForm(SetPasswordForm):
    """Форма изменения пароля"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

