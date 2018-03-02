from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Idea, Criterion

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'description')
        labels = {'title': _('Título'), 'description': _('Descrição'), }

class IdeaFormUpdate(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'description', 'phase')
        labels = {'title': _('Título'), 'description': _('Descrição'), 'phase': _('Fase'), }

class CriterionForm(forms.ModelForm):

    class Meta:
        model = Criterion
        fields = ('description','peso')
        labels = {'peso': _('Peso'), 'description': _('Descrição'), }
