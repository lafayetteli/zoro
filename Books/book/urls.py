from django.conf.urls import url
from . import views
upatternsrl = [
    url(r'^books$',views.BooksView.as_view(),name='books'),
    url(r'^book$(?P<pk>\d+)',views.BookView.as_view(),name='book'),
]