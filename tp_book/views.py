from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from BookShop.api_utilities import Message
from tp_book.models import *
from tp_book.serializers import *


class GetAllData(APIView):
    def get(self,request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request':request}) # set context for be url image field in responsed json data
        return Response(serializer.data, status=200)


class DetailData(APIView):
    def get(self,request, pk):
        try:
            queryset = Book.objects.get(pk=pk)
            serializer = BookSerializer(queryset, context={'request':request}) # set context for be url image field in responsed json data
            return Response(Message.found(request, serializer.data), status=status.HTTP_302_FOUND)
        except Book.DoesNotExist:
            return Response(Message.error(request, f'Not found data for `{pk}` primary key'), status=404)

    def put(self, request, pk):
        try:
            queryset = Book.objects.get(pk=pk)
            serializer = BookSerializer(queryset, data=request.data, context={'request':request}) # set context for be url image field in responsed json data
            if serializer.is_valid():
                serializer.save()
                return Response(Message.updated(request, serializer.data), status=201)
            return Response(Message.error(request, message='not valid data', errors=serializer.errors, data=request.data), status=406)
        except Book.DoesNotExist:
            return Response(Message.error(request, f'Not found data for `{pk}` primary key'), status=404)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            book.delete()
            return Response(Message.deleted(request, serializer.data), status=status.HTTP_202_ACCEPTED)
        except Book.DoesNotExist:
            return Response(Message.error(request, f'Not found data for `{pk}` primary key.'), status=404)



class CreateData(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Message.created(request, serializer.data), status=201)
        return Response(Message.error(request, 'not valid data',data=serializer.data, errors=serializer.errors), status=406)

    # def post(self, request):
    #     serializer:BookSerializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         author = serializer.validated_data.get('author')
    #         name = serializer.validated_data.get('name')
    #         desc = serializer.validated_data.get('desc')
    #         fav = serializer.validated_data.get('fav')
    #         image= serializer.validated_data.get('image')
    #         Book.objects.create(author=author, name=name, desc=desc, fav=fav, image=image)
    #         return Response(Message.created(request, serializer.data), status=201)
    #     return Response(Message.error(request, 'not valid data',data=serializer.data, errors=serializer.errors), status=406)


class SerachData(APIView):
    def get(self, request):
        author       =   request.GET.get('author', default='')
        name       =   request.GET.get('name', default='')
        lookup = (
            # Q(desc__icontains=name) |
            # Q(desc__icontains=author) |
            Q(author__icontains=author) |
            Q(name__icontains = name)
        )
        books        =   Book.objects.filter(lookup).distinct()
        serializer   =   BookSerializer(books, many=True)
        return Response(Message.found_data(request, serializer.data), status=status.HTTP_302_FOUND)


@api_view()
def get_fav_data(request):
    queryset = Book.objects.filter(fav=True)
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data, status=200)


