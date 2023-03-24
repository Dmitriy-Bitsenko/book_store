from django import forms
from .models import book


class BookForm(forms.ModelForm):
    class Meta:
        model = book

        fields = ['title', 'description', 'count_pages', 'price', 'cover_type', 'size']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название книги',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание книги',
                }
            ),
            'count_pages': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Количество страниц',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Цена',
                }
            ),
            'size': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Размер книги',
                }
            ),
            'cover_type': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Тип обложки',
                }
            ),
        }
