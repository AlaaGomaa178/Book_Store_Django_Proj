from django.urls import path  
from . import views  

# List of URL patterns for mapping URLs to views
urlpatterns = [  
    
     # URL pattern for the home page, mapped to the home view function
    path('', views.home, name='home'), 
    
    # URL pattern for displaying all books, mapped to the all_books_from_list view function
    path('all_books/', views.all_books_from_list, name='all_books'),  
    
    # URL pattern for showing details of a book, mapped to the show_book view function with a parameter 'book_id'
    path('show_book/<int:id>/', views.show_book, name='show_book'),  
 
    path('add_book/', views.create_books, name='create_books'),
    
    path('all_books/<int:id>/', views.book_delete, name='book_delete'),
    
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),



]
