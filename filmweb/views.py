from django.shortcuts import render, redirect

# Create your views here.
from filmweb.models import Person, Movie


def person_view(request):
    objects = Person.objects.all()
    return render(request, "show_objects.html", {'objects': objects})

def movie_view(request):
    objects = Movie.objects.all()
    return render(request, 'show_objects.html', {'objects':objects})

def add_movie_view(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        return render(request, 'add_movie.html', {'persons':persons})
    else:
        title = request.POST['title']
        year = request.POST['year']
        person_id = request.POST['directed_by']
        person = Person.objects.get(id = person_id)
        Movie.objects.create(title=title, year=year, directed_by=person)
        return redirect("/movies/")

def add_person_view(request):
    if request.method == 'GET':
        return render(request, 'add_person.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Person.objects.create(first_name=first_name, last_name=last_name)
        return redirect('/persons/')
