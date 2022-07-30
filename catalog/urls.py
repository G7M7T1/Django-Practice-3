from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-book/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('views/', views.my_view, name='views'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.CheckOutBookByUser.as_view(), name='profile')
]