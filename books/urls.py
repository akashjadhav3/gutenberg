from django.urls import path
from .views import *
urlpatterns = [    
    path('books/', BookView.as_view(),name='books_list'),
    path('books/<int:gutenberg_id>/', BookView.as_view(),name='books_details'),
]