from django import forms
from .models import Issue, Item
from .models import Csv

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields =('file_name',)

class Itemlist(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name', 'quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['numberofitems']


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name', 'quantity']
        model.created_number = Item.quantity



        def clean_category(self):
            category = self.cleaned_data.get('category')
            if not category:
                raise forms.ValidationError('This field is required')
            return category

        def clean_item_name(self):
            item_name = self.cleaned_data.get('item_name')
            if not item_name:
                raise forms.ValidationError('This field is required')
            return item_name


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name', 'quantity']
