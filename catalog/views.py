from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book, Author, BookInstance, Genre, Language
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


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


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    model = Book


@login_required
def my_view(req):
    return render(req, 'catalog/views.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckOutBookByUser(LoginRequiredMixin, ListView):
    # List All BookInstances
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5  # 5 Book Per Page Display

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).all()
