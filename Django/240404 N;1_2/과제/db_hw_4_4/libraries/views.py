from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    form = ReviewForm()
    context = {
        'book': book,
        'reviews':reviews,
        'form':form,
    }
    return render(request, 'libraries/detail.html', context)

def create_comment(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('libraries:detail', book_pk)
    else:
        form = ReviewForm()
    context = {
        'reviews':reviews,
        'form':form,
        'book':book,
    }
    return render(request, 'libraries/detail.html', context)

def delete_comment(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('libraries:detail', book_pk)
