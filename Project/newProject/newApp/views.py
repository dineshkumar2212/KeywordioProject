from newApp.serializers import BookSerializer
from .models import Book
from rest_framework import generics
from django.shortcuts import render

def index(request):
    return render(request,'newApp/index.html')
    
class StudentListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

