from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from filmweb.forms import LoginForm, RegisterForm, UserEditForm
from filmweb.models import Person, Movie, Country, Studio


def index(request):
    return render(request, 'base.html')

def person_view(request):
    objects = Person.objects.all()
    sikorka = render(request, "show_objects.html", {'object_list': objects})
    return sikorka

class PersonListView(View):

    def get(self, request):
        objects = Person.objects.all()
        nazwisko = request.GET.get('data')
        if nazwisko is not None:
            objects = objects.filter(last_name__icontains=nazwisko)
        sikorka = render(request, "show_objects.html", {'object_list': objects})
        return sikorka

def movie_view(request):
    objects = Movie.objects.all()
    return render(request, 'show_objects.html', {'object_list':None})


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
        return render(request, 'add_movie.html', {'persons':persons, 'cos':['dasf','dfas'], })
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



def add_info_to_session(request):
    if request.method == "POST":
        key = request.POST['session_key']
        value = request.POST['session_value']
        request.session[key] = value
    return render(request, 'session.html', {'session':request.session.items()})


def add_cookie(request):
    response = render(request, 'cookie.html', {'jabuszko': request.COOKIES.items()})
    if request.method == "POST":
        key = request.POST['cookie_key']
        value = request.POST['cookie_value']
        response.set_cookie(key, value, max_age=3)
    return response



class AddCountryView(PermissionRequiredMixin, View):
    permission_required = ('filmweb.add_country',)

    def get(self, request):
        return render(request,  'add_country.html')

    def post(self, request):
        name = request.POST['name']
        Country.objects.create(name=name)
        return redirect(reverse("country_list"))

class CountryView(View):
    def get(self, request):
        return render(request, 'show_objects.html', {'object_list': Country.objects.all()})


class StudioMovieView(View):

    def get(self, request, id, year, title):
        studio = Studio.objects.get(id=id)
        movies = Movie.objects.filter(studio=studio, year=year, title__startswith=title)
        return render(request, 'show_objects.html', {'object_list':movies})


class AddStudioView(View):

    def get(self, request):
        countries = Country.objects.all()
        return render(request, 'add_studio.html', {'kraje':countries})

    def post(self, request):
        nazwa = request.POST['nazwa']
        kraj_id = request.POST['country']
        kraj = Country.objects.get(id=kraj_id)
        Studio.objects.create(name=nazwa, country=kraj)
        return redirect(reverse('studio_list'))

class StudioListView(LoginRequiredMixin, View):

    def get(self, request):

        pobrane_studia_z_bazy = Studio.objects.all()
        nazwa = request.GET.get('data')
        if nazwa is not None:
            pobrane_studia_z_bazy = pobrane_studia_z_bazy.filter(name__icontains=nazwa)
        return render(request, 'show_objects.html', {'object_list':pobrane_studia_z_bazy})

class StudioDetailView(View):

    def get(self, request, id):
        countries = Country.objects.all()
        studio = Studio.objects.get(id=id)
        return render(request, 'detail_studio.html', {'kraje': countries, 'wytwornia':studio})

    def post(self, request, id):
        studio = Studio.objects.get(id=id)
        nazwa = request.POST['nazwa']
        kraj_id = request.POST['country']
        kraj = Country.objects.get(id=kraj_id)
        studio.name = nazwa
        studio.country = kraj
        studio.save()
        return redirect(reverse('studio_list'))


class ListUserView(ListView):
    model = User
    template_name = 'show_user.html'


class UserDetailView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, id):
        user = User.objects.get(pk = id)
        form = UserEditForm(instance=user)
        return render(request, 'form.html', {'form':form})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form': form})

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', 'index')
                #próbujemy pobrać ze słownika request.GET wartość która znajduje sie pod kluczem "next" jesli nie ma 'next'
                # to zwracamy "index"
                return redirect(redirect_url)
            else:
                return redirect('login')

        # dzięki wywołaniu metody is_valid na obiekcie form tworzy na sie słowniki w obiekcie form o nazwie
        # cleaned_data w którym przechowywane sa wszystkie pola z formlularza.
        # form.cleaned_data = {
        #     'username': request.POST['username'],
        #     'password': request.POST['password']
        # }
        # metoda authenticate wyglada tak ze przyjmuje trzy paramaetry request, username, password
        # mógłbym napisać to authenticate(request,
        #                                 username = form.cleaned_data['username'],
        #                                 password = form.cleaned_data['password'])
        # natomiast użycie ** gwiazdek na słowniku cleaned_data przy wowłaniu funkcji jakby rozpisuje słownik na
        # takie użycie jak jest pokazane powyżej


class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')




class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            u = User.objects.create(username=username)
            u.set_password(password)
            u.save()
            return redirect('login')
        else:
            return render(request, 'form.html', {'form': form})

