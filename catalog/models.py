from django.db import models
import uuid
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Language(models.Model):
    lang = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.lang}'


class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=300)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)
    lang = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=60)
    due_back = models.DateField(null=True, blank=True)
    loan_status = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=loan_status, blank=True, default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} | {self.book.title}'
