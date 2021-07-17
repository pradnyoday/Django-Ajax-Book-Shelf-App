from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    name  = forms.CharField(max_length=250,label='',widget=forms.TextInput(attrs={'placeholder': "Book's Name",'class':'form-control mt-2','id':'name'}), required=True)
    author = forms.CharField(max_length=250,label='',widget=forms.TextInput(attrs={'placeholder': "Author's Name",'class':'form-control mt-2','id':'author'}), required=True)
    class Meta:
        model = Book
        fields = ['id', 'name', 'author']
        