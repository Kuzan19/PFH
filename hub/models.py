from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, FileExtensionValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class HubDoggyModel(models.Model):
    """Таблица объявлений в базе данных"""

    GENDER_DOGGY = [
        ('Boy', "Boy"),
        ('Girl', "Girl")
    ]

    name = models.CharField(max_length=255, blank=False, null=False)
    age_old = models.IntegerField(blank=False, null=False, validators=[MaxValueValidator(22)])
    months_old = models.IntegerField(blank=False, null=False, validators=[MaxValueValidator(12)])
    gender = models.CharField(max_length=4, choices=GENDER_DOGGY, default="Boy")
    place = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(default='', null=False, db_index=True)
    price = models.IntegerField(blank=True, null=False, validators=[MinValueValidator(1)], default=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='doggy')
    species = models.CharField(max_length=255, blank=False, null=False, default='')

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}{self.age_old}{self.months_old}")
        super(HubDoggyModel, self).save(*args, **kwargs)

    def get_url(self):
        """Функция возвращает url объекта (в данном случае обращение по id и slug)"""
        return reverse("hub_page", args=[self.id, self.slug])


class PhotoDoggyModel(models.Model):
    image = models.FileField(upload_to='uploads/DoggyPhoto')
    doggy = models.ForeignKey(HubDoggyModel, on_delete=models.CASCADE, null=True, blank=True, related_name='photos')

    def __str__(self):
        return f"id: {self.doggy}"



