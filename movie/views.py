from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.core.files.storage import default_storage
from .form import MovieForm, CollageForm
from .models import Movie, Collage
import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64
from itertools import islice
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


def chunk(iterable, size):
    it = iter(iterable)
    item = list(islice(it, size))
    while item:
        yield item
        item = list(islice(it, size))


def collage(request):
    form = CollageForm()
    if request.method == 'POST':
        form = CollageForm(request.POST, request.FILES)
        obj = Collage.objects.first()
        if form.is_valid():
            file = request.FILES['image']
            file_name = default_storage.save(file.name, file)
            file_url = default_storage.url(file_name)
            obj.list_obj['image'].append(file_url)
            obj.save()

    obj = Collage.objects.first()
    list_default = obj.list_obj['image']
    if len(list_default) % 6 != 0:
        num = 6 - len(list_default) % 6
        for i in range(0,num):
            list_default.append('')

    out_image = list(chunk(list_default,6))

    context = {'form': form, 'out_image': out_image}

    return render(request, 'movie/collage.html', context)

def clear_collage(request):
    obj = Collage.objects.first()
    obj.list_obj = {'image':[]}
    obj.save()

    return redirect('collage')


def display_graph1(request):
    try:
        if request.GET['z']:
            z = int(request.GET['z'])
    except:
        z = 3

    x = np.arange(-3, 3, 0.1)
    y = x ** z
    plt.title(f'y=x^{z}')
    plt.grid(True)
    plt.plot(x, y)

    fig = plt.gcf()
    fig.set_size_inches(3, 3)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    context = {'data': uri}
    fig.clear()
    return render(request, 'movie/display_graph.html', context)


def display_graph2(request):
    x = 30
    y = 30
    z = 40
    try:
        if request.GET['x'] and request.GET['y'] and request.GET['z']:
            x = int(request.GET['x'])
            y = int(request.GET['y'])
            z = int(request.GET['z'])
    except:
        z = 30
        y = 30
        z = 40

    size_of_groups = [x, y, z]
    colors = ["orange", "green", "black"]
    labels = [f'x = {x}', f'y= {y}', f'z = {z}']
    plt.pie(size_of_groups, colors=colors, labels=labels)
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    fig = plt.gcf()
    fig.set_size_inches(3, 3)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    context = {'data': uri}
    fig.clear()
    return render(request, 'movie/display_graph2.html', context)
