from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Idea, Criterion, Category, Dimension, Category_Dimension, Evaluation

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('title', 'summary', 'oportunity', 'solution', 'target', 'category' )
        labels = {'title': _('Title'), 'summary': _('Summary') , 'oportunity': _('Oportunity'), 'solution': _('Solution'), 'target': _('Target'),'category': _('Category')}
        widgets = {
            'summary': forms.Textarea(attrs={'placeholder': _('Sell your idea in 140 characters!')}),
            'oportunity': forms.Textarea(attrs={'placeholder': _('Describe the problem or opportunity your idea will meet!')}),
            'solution': forms.Textarea(attrs={'placeholder': _('Describe the solution very clearly and succinctly!')}),
            'target': forms.Textarea(attrs={'placeholder': _('Indicate who your solution audience is')}),
        }


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

class EvaluationForm(forms.Form):
    FORMAT_ID = 'category_dimension_%s'
    FORMAT_ID_NOTE = 'note_dimension_%s'

    def __init__(self, *args, **kwargs):
        dimensions = kwargs.pop('extra', None)
        initial_arguments = kwargs.pop('initial', None)
        super(EvaluationForm, self).__init__(*args, **kwargs)

        if initial_arguments:
            for i in initial_arguments:
                id_field = self.FORMAT_ID % initial_arguments[i].dimension.pk
                self.fields[id_field] = forms.ModelChoiceField(queryset=initial_arguments[i].dimension.category_dimension_set,
                                                                                                         label=initial_arguments[i].dimension.title,
                                                                                                         initial=initial_arguments[i].category_dimension.id,
                                                                                                         help_text=initial_arguments[i].dimension.description)

                id_field_note = self.FORMAT_ID_NOTE % initial_arguments[i].dimension.pk
                self.fields[id_field_note] = forms.CharField(initial=initial_arguments[i].note,
                                                             widget=forms.Textarea,
                                                             label='',
                                                             required=False)
        if dimensions:
            for dim in dimensions:
                self.fields[self.FORMAT_ID % dim.pk ] = forms.ModelChoiceField(queryset=dim.category_dimension_set,
                                                                               label=dim.title,
                                                                               help_text=dim.description)
                self.fields[self.FORMAT_ID_NOTE % dim.pk] = forms.CharField(widget=forms.Textarea,
                                                                            label='',
                                                                            required=False)
