from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Idea, Criterion, Category

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'description', 'category' )
        labels = {'title': _('Título'), 'description': _('Descrição'), 'category': _('Categoria')}


class IdeaFormUpdate(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'description')
        labels = {'title': _('Title'), 'description': _('Description'),  }

class CriterionForm(forms.ModelForm):

    class Meta:
        model = Criterion
        fields = ('description','peso')
        labels = {'peso': _('Weight'), 'description': _('Description'), }

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('description', 'key_word', )
        labels = {'description': _('Description'), 'key_word':_('key_word') }
