from django import forms
from .models import *

class ProductSearchForm(forms.Form):
    query            = forms.CharField(label='Search Product', max_length=100, required=False)
    category         = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='All Categories', required=False)
    subcategory      = forms.ModelChoiceField(queryset=SubCategory.objects.all(), empty_label='All Sub Categories', required=False)
    super_subcategory= forms.ModelChoiceField(queryset=Super_SubCategory.objects.all(), empty_label='All Super Sub Categories', required=False)
    size             = forms.ModelChoiceField(queryset=Size.objects.all(), empty_label='All Sizes', required=False)
    color            = forms.ModelChoiceField(queryset=Color.objects.all(), empty_label='All Colors', required=False)
    condition        = forms.ModelChoiceField(queryset=Condition.objects.all(), empty_label='All Conditions', required=False)
