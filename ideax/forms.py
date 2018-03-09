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
        labels = {'title': _('Título'), 'description': _('Descrição'),  }

class CriterionForm(forms.ModelForm):

    class Meta:
        model = Criterion
        fields = ('description','peso')
        labels = {'peso': _('Peso'), 'description': _('Descrição'), }

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('description', 'key_word', )
        labels = {'description': _('Descrição'), 'key_word':_('Palavra-chave') }
