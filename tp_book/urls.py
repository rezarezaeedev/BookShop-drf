from django.urls import path

from tp_book.views import *

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('detail-data/<pk>/', DetailData.as_view()),
    path('get-fav-data/', get_fav_data),
    path('create-data/', CreateData.as_view()),
    path('search/', SerachData.as_view()),
]




