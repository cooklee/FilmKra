from django.shortcuts import render, redirect
# Create your views here.
from filmweb.models import Person, Movie


def index(request):
    return render(request, 'base.html')

def person_view(request):
    objects = Person.objects.all()
    sikorka = render(request, "show_objects.html", {'objects': objects})
    return sikorka

def movie_view(request):
    objects = Movie.objects.all()
    return render(request, 'show_objects.html', {'objects':objects})


def detail_person_view(request, id):
    object = Person.objects.get(id=id)
    if request.method == 'GET':
        return render(request, "person_detail.html", {'person':object})



def detail_movie_view(request, id):
    object = Movie.objects.get(id=id)
    persons = Person.objects.all()
    if request.method == 'GET':
        return render(request, "movie_detail.html",  {'movie':object, 'persons':persons})
    else:
        title = request.POST['title']
        year = request.POST['year']
        person_id= request.POST['directed_by']
        pp = Person.objects.get(id=person_id)
        object.title = title
        object.year = year
        object.directed_by = pp
        object.save()
        actors = request.POST.getlist('actors')
        object.actors.set(actors)
        return redirect("/movies/")



def add_movie_view(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        return render(request, 'add_movie.html', {'persons':persons})
    else:
        title = request.POST['title']
        year = request.POST['year']
        person_id = request.POST['directed_by']
        person = Person.objects.get(id = person_id)
        movie = Movie.objects.create(title=title, year=year, directed_by=person)
        actors_id = request.POST.getlist('actors')
        actors = Person.objects.filter(id__in=actors_id)
        #movie.actors.set(actors)
        for actor in actors:
            movie.actors.add(actor)
        return redirect("/movies/")

def add_person_view(request):
    if request.method == 'GET':
        return render(request, 'add_person.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Person.objects.create(first_name=first_name, last_name=last_name)
        return redirect('/persons/')
