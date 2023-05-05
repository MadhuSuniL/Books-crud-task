from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book

class FirstView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class SecondView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    
def IndexView(request):
    books = Book.objects.all().reverse()
    
    data = {
        'books':books,
        'total':books.count()
    }
    for book in books:
        print(book.cover_image)
        
    return render(request, 'index.html',context=data)