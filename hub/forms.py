from django import forms
from hub.models import HubDoggyModel, PhotoDoggyModel
from django.forms.models import inlineformset_factory


class HubDoggyForm(forms.ModelForm):
    """Форма добавления объявлений"""
    class Meta:
        model = HubDoggyModel
        fields = "__all__"
        exclude = ('slug', )
        widgets = {'seller': forms.HiddenInput()}


class PhotoDoggyForm(forms.ModelForm):
    class Meta:
        model = PhotoDoggyModel
        fields = "__all__"
        exclude = ('doggy', )
    

AddDoggyFormSet = inlineformset_factory(HubDoggyModel, PhotoDoggyModel, form=PhotoDoggyForm, extra=1)

