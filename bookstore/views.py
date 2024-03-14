from django.shortcuts import render, redirect, reverse
from django.conf import settings 
from .models import Books
from django.http import HttpResponse
# from datetime import datetime


def home(request):
    
    """View function for rendering the home page."""
    return render(request, 'bookstore/home.html')  

"""
def all_books_from_list(request):
    
    View function for rendering all books page.
    
    # list of dictionaries of data of the books
    books = [
        {"title": "Harry Potter", "author": "J. K. Rowling", "price": 10.99, "pages": 200, "image": "book 1.jpg"},
        {"title": "Oliver Twist", "author": "William Shakspeare", "price": 12.99, "pages": 150, "image": "book 2.jpg"},
        {"title": "Memory", "author": "Angeline Ludo 3", "price": 15.99, "pages": 300, "image": "book 3.jpg"},
        {"title": "Romeo and Juliet", "author": "William Shakspeare", "price": 15.99, "pages": 300, "image": "book 4.jpg"},
    ]
    
    # Prepending STATIC_URL to each book image path
    for book in books:
        book['image'] = settings.STATIC_URL + book['image']
        
    # Rendering the all books template with the books data
    return render(request, 'bookstore/all_books.html', {'books': books})



def show_book(request, book_id):
    
    View function for showing details of a specific book.
    books = [
        {"title": "Harry Potter", "author": "J. K. Rowling", "price": 10.99, "pages": 200, "image": "book 1.jpg"},
        {"title": "Oliver Twist", "author": "William Shakspeare", "price": 12.99, "pages": 150, "image": "book 2.jpg"},
        {"title": "Memory", "author": "Angeline Ludo ", "price": 15.99, "pages": 300, "image": "book 3.jpg"},
        {"title": "Romeo and Juliet", "author": "William Shakspeare", "price": 15.99, "pages": 300, "image": "book 4.jpg"},
    ]
    
    book = None
    
    try:
        book = books[book_id]  # Get the book with the given book_id
        
        book['image'] = settings.STATIC_URL + book['image']  
        
    except IndexError:
        pass

    if book:  # If book found
        return render(request, 'bookstore/show_book.html', {'book': book})  # Render show book template with book data
    else:
        return render(request, 'bookstore/error.html', {'message': 'Book not found'})  # Render error template with error message
"""
    
def all_books_from_list(request):
    books = Books.objects.all()  # Retrieve all books from the database
    return render(request, 'bookstore/all_books.html', {'books': books})

def show_book(request, id):
    book = Books.objects.get(id=id)
    if book:
        return render(
            request, "bookstore/show_book.html", context={"book": book}
        )
    return HttpResponse("book doesn't exist")


def create_books(request):
    if request.method == 'POST':
        title = request.POST["Title"]
        author = request.POST["Author"]
        price = request.POST['Price']
        pages = request.POST["Number of Pages"]

        book = Books(title=title, author=author, price=price, pages=pages, image=request.FILES['image'])
        book.save()

        return redirect('all_books')  

    return render(request, 'bookstore/add_book.html')


def book_delete(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('all_books')  

def edit_book(request, id):
    # Fetch the existing book object from the database
    book = Books.objects.get(id=id)
    #current_time = datetime.now()

    if request.method == 'POST':
        # Update the book object with the new data from the form
        book.title = request.POST["Title"]
        book.author = request.POST["Author"]
        book.price = request.POST['Price']
        book.pages = request.POST["Number of Pages"]
        book.image = request.FILES['image'] if 'image' in request.FILES else book.image
        book.save()

        return redirect('all_books')  

    # render the form with existing book details
    return render(request, 'bookstore/edit_book.html', {'book': book})
    #return render(request, 'bookstore/edit_book.html', {'book': book, 'current_time': current_time})

