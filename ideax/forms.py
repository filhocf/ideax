from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Idea, Criterion, Category

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'oportunity', 'solution', 'target', 'category' )
        labels = {'title': _('Title'), 'oportunity': _('Oportunity'), 'solution': _('Solution'), 'target': _('Target'),'category': _('Category')}


class IdeaFormUpdate(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'oportunity', 'solution', 'target')
        labels = {'title': _('Title'), 'oportunity': _('Oportunity'), 'solution': _('Solution'), 'target': _('Target'),  }

class CriterionForm(forms.ModelForm):

    class Meta:
        model = Criterion
        fields = ('description','peso')
        labels = {'peso': _('Weight'), 'description': _('Description'), }

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title', 'description', )
        labels = {'title':_('Title'), 'description': _('Description') }
