from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


User = get_user_model()


class Profile(models.Model):

    """Model for registration and keep information about users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='uploads/avatars/%Y/%m/%d/',
        default='uploads/avatars/default.jpg',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self, self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        """Возвращение строки"""
        return self.user.username

    def get_url(self):
        """Функция возвращает url объекта (в данном случае обращение по id и slug)"""
        return reverse("profile_page", args=[self.slug])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

