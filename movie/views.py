from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from .form import MovieForm
from .models import Movie

import json


# Create your views here.
def main_movie(request):
    movies = Movie.objects.all()

    try:
        if request.GET['filter']:
            movies = Movie.objects.filter(title__icontains=request.GET['filter'])
    except:
        context = {'movies': movies}
        return render(request, 'movie/main.html', context)

    context = {'movies': movies}
    return render(request, 'movie/main.html', context)


def add_movie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        file = json.loads(request.FILES['txt'].read())
        try:
            movie = Movie.objects.create(title=file['Title'],
                                         year=file['Year'],
                                         imdbID=file['imdbID'],
                                         poster=request.FILES['poster'],
                                         rated=file['Rated'],
                                         released=file['Released'],
                                         runtime=file['Runtime'],
                                         genre=file['Genre'],
                                         director=file['Director'],
                                         writer=file['Writer'],
                                         actors=file['Actors'],
                                         plot=file['Plot'],
                                         language=file['Language'],
                                         country=file['Country'],
                                         awards=file['Awards'],
                                         imdbRating=file['imdbRating'],
                                         imdbVotes=file['imdbVotes'],
                                         type=file['Type'],
                                         production=file['Production'],
                                         txt='')
        except:
            messages.info(request, 'An error occurred while processing your request, this film already exist!')
            return redirect('main_movie')
        return redirect('main_movie')

    context = {'form': form}
    return render(request, 'movie/add_movie.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    slug_field = 'imdbID'


def delete_movie(request, pk):
    post = Movie.objects.get(id=pk)
    if request.method == 'GET':
        post.delete()
        return redirect('/')
