from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Idea, Phase, Criterion

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'description')
        labels = {'title': _('Título'), 'description': _('Descrição'), }

class PhaseForm(forms.ModelForm):

    class Meta:
        model = Phase
        fields = ('name','description')
        labels = {'name': _('Nome'), 'description': _('Descrição'), }

class CriterionForm(forms.ModelForm):

    class Meta:
        model = Criterion
        fields = ('description','peso')
        labels = {'peso': _('Peso'), 'description': _('Descrição'), }
