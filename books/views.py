from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

#pagination class
class MyPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class BookView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    """ This is an API endpoint allows to view books """
    serializer_class = BookSerializer
    lookup_field = 'gutenberg_id'
    queryset = Book.objects.all().order_by('-download_count')
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = self.queryset

        id = self.request.GET.get('id')
        if id is not None:
            queryset = queryset.filter(gutenberg_id=id)

        languages = self.request.GET.get('languages')
        if languages is not None:
            languages_list = [code.lower() for code in languages.split(',')]
            queryset = queryset.filter(languages__code__in=languages_list)

        author = self.request.GET.get('author')
        if author is not None:
            queryset = queryset.filter(authors__name__icontains=author)

        title = self.request.GET.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        mime_type = self.request.GET.get('mime_type')
        if mime_type is not None:
            queryset = queryset.filter(format__mime_type__icontains=mime_type)

        topic = self.request.GET.get('topic')
        if topic is not None:
            queryset = queryset.filter(
                Q(bookshelves__name__icontains=topic) | Q(subjects__name__icontains=topic)
            )
        return queryset

    def get(self, request,gutenberg_id=None):
        if gutenberg_id:
            return self.retrieve(request,gutenberg_id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def delete(self,request,gutenberg_id=None):
        return self.destroy(request,gutenberg_id)

    def put(self,request,gutenberg_id=None):
        return self.update(request,gutenberg_id)


def home(request):
    return render(request, 'books/home.html',context={})