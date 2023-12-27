from . import views
from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    #path('', views.home,name='home'),
    path('', views.MyTemplateView.as_view(template_name='home.html'),{'author':'Miguel'},name='home'),
    path('<int:roll>', views.MyTemplateView.as_view(template_name='home.html'),{'author':'Miguel'},name='home'),
    #path('', views.MyTemplateView.as_view(template_name='home.html'),name='home'),
    #path('Store_Books/', views.store_books,name='store_book'),
    path('Store_Books/', views.Bookformview.as_view(),name='store_book'),
    #path('Show_Books/', views.show_books,name='show_books'),
    path('Show_Books/', views.Booklistview.as_view(),name='show_books'),
    path('Book Details/<int:id>', views.BookDetailsView.as_view(),name='book_details'),
    #path('Edit_Books/<int:id>', views.edit_book,name='edit_book'),
    path('Edit_Books/<int:pk>', views.Bookupdateview.as_view(),name='edit_book'),
    #path('Delete_Books/<int:id>', views.delete_book,name='delete_book'),   
    path('Delete_Books/<int:pk>', views.Deletebookview.as_view(),name='delete_book'),   
]