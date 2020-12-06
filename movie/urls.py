from django.urls import path
from .views import *

urlpatterns = [
    path('', main_movie, name='main_movie'),
    path('main_api', main_movie_api, name='main_movie_api'),
    path('add', add_movie, name='add_movie'),
    path('graph', display_graph1, name='graph'),
    path('diagram', display_graph2, name='diagram'),
    path('collage', collage, name='collage'),
    path('collage_api', collage2, name='collage_api'),
    path('clear_collage',clear_collage, name='clear_collage'),
    path('<str:slug>', MovieDetailAPIView.as_view(), name='detail_movie_api'),

    path('<str:slug>', MovieDetailView.as_view(), name='detail_movie'),
    path('delete/<str:pk>/', delete_movie, name='delete_movie'),

    # path('filter', filter_movie, name='filter_movie'),

]
