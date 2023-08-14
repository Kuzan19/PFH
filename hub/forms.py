from django import forms
from hub.models import HubDoggyModel, PhotoDoggyModel
from django.forms.models import inlineformset_factory


class HubDoggyForm(forms.ModelForm):
    """Форма добавления объявлений"""
    class Meta:
        model = HubDoggyModel
        fields = "__all__"
        exclude = ('slug', )


class PhotoDoggyForm(forms.ModelForm):
    class Meta:
        model = PhotoDoggyModel
        fields = "__all__"


# AddDoggyFormSet = inlineformset_factory(HubDoggyModel, PhotoDoggyModel, form=PhotoDoggyForm,  extra=1,
#                                         can_delete=True, can_delete_extra=True)

