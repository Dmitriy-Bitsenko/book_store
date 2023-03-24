from django.shortcuts import render, get_object_or_404
from .models import book
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import BookForm


def index(request):
    return render(request=request, template_name='book_store/index.html')


def book_catalog(request):
    context = {'all_books': book.objects.all()}
    return render(request=request, template_name='book_store/book/list.html', context=context)


def book_description(request, book_id):
    one_book = get_object_or_404(book, pk=book_id)
    return render(request=request, template_name='book_store/book/info.html', context={'one_book': one_book})


class BookCreateView(CreateView):
    model = book
    form_class = BookForm
    template_name = 'book_store/book/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = book
    form_class = BookForm
    template_name = 'book_store/book/update.html'
    context_object_name = 'form'






