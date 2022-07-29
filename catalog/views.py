from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre, Language


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_ava = BookInstance.objects.filter(status__exact='a')
    return HttpResponse('hello')
