from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_author = Author.objects.all().count()
    num_lang = Language.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_a = BookInstance.objects.filter(status__exact='a').count()
    num_instances_m = BookInstance.objects.filter(status__exact='m').count()
    num_instances_o = BookInstance.objects.filter(status__exact='o').count()
    num_instances_r = BookInstance.objects.filter(status__exact='r').count()

    context = {
        'num_lang': num_lang,
        'num_book': num_books,
        'num_author': num_author,
        'num_instances': num_instances,
        'num_instances_a': num_instances_a,
        'num_instances_m': num_instances_m,
        'num_instances_o': num_instances_o,
        'num_instances_r': num_instances_r
    }
    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    model = Book
