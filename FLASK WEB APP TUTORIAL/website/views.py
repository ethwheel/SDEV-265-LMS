from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Book  # Import the Book model
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    print ("here")
    query = request.args.get('query', '').strip()
    print (query)
    # Fetch books based on search query
    if query:
        books = Book.query.filter(
            Book.title.contains(query) | 
            Book.author.contains(query) | 
            Book.isbn.contains(query)
        ).all()
    else:
        books = Book.query.all()
        
    print(books)
    return render_template("home.html", user=current_user, books=books)

@views.route('/checkout/<bookId>', methods=['GET', 'POST'])
@login_required
def checkout_book(bookId):

    books = Book.query.filter(Book.id == bookId)

    # get book
    # update 'available' property
    # return updated list of books

    return render_template("home.html", user=current_user, books=books)