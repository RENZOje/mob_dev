from django.urls import path
from .views import *

urlpatterns = [
    path('', main_movie, name='main_movie'),
    path('add', add_movie, name='add_movie'),
    path('<str:slug>', MovieDetailView.as_view(), name='detail_movie'),
    path('delete/<str:pk>/', delete_movie, name='delete_movie'),
    # path('filter', filter_movie, name='filter_movie'),

]
