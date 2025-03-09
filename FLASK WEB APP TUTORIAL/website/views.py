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

    # temporarily just show book selected for checkout -- remove once available property is updated correctly
    #books = Book.query.filter(Book.id == bookId)

    # get book
    books = Book.query.get(bookId)
    # update 'available' property
    
    books.available = 0
    
    db.session.commit()
    # return updated list of books
    books = Book.query.all()
    return render_template("home.html", user=current_user, books=books)

@views.route('/checkin/<bookId>', methods=['GET', 'POST'])
@login_required
def checkin_book(bookId):

    # temporarily just show book selected for checkout -- remove once available property is updated correctly
    #books = Book.query.filter(Book.id == bookId)

    # get book
    books = Book.query.get(bookId)
    # update 'available' property
    
    books.available = 1
    
    db.session.commit()
    # return updated list of books
    books = Book.query.all()
    return render_template("home.html", user=current_user, books=books)