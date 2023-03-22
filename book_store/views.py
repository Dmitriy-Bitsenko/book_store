from django.shortcuts import render, get_object_or_404
from .models import book


def index(request):
    return render(request=request, template_name='book_store/index.html')


def book_catalog(request):
    context = {'all_books': book.objects.all()}
    return render(request=request, template_name='book_store/book/list.html', context=context)


def book_description(request, book_id):
    one_book = get_object_or_404(book, pk=book_id)
    return render(request=request, template_name='book_store/book/info.html', context={'one_book': one_book})




