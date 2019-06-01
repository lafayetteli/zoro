from django.shortcuts import render
from django.views import View
from .serializers import BookSerializer
from django.http import JsonResponse,Http404
from .models import BookInfo
import json
class BooksView(View):
    def post(self,request):
        pram_dict = json.loads(request.body.decode())
        serializers = BookSerializer(data=pram_dict)
        if serializers.is_valid():
            book = serializers.save()
            serializers = BookSerializer(book)
            book_dict = serializers.data
            return JsonResponse(book_dict,status=201)
        else:
            return JsonResponse(serializers.errors)
class BookView(View):
    def get(self,request,pk):
        book = BookInfo.objects.get(pk=pk)
        serializers = BookSerializer(book)
        book_date = serializers.data
        return JsonResponse(book_date)
    def put(self,request,pk):
        pram_dict = json.loads(request.body.decode())
        book = BookInfo.objects.get(pk=pk)
        serializers = BookSerializer(book,data=pram_dict)
        if serializers.is_valid():
            book.save()
            serializers = BookSerializer(book)
            book_dict = serializers.data
            return  JsonResponse(book_dict,status=201)
        else:
            return JsonResponse(serializers.errors)


