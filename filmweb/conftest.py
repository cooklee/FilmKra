import pytest
from django.test import Client
from django.contrib.auth.models import User, Permission

from filmweb.models import Person, Country, Studio, Movie


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def users():
    users = []
    for x in range(1, 11):
        u = User.objects.create(username=str(x))
        users.append(u)
    return users

@pytest.fixture
def user_with_permissions():
    u = User.objects.create(username='aabb')
    permissions = Permission.objects.filter(content_type_id__gte=3)
    #Permission.objects.get(codename='add_studio')
    for p in permissions:
        u.user_permissions.add(p)
    return u

@pytest.fixture
def persons():
    persons = []
    for x in range(1, 11):
        u = Person.objects.create(first_name=str(x), last_name='dudek')
        persons.append(u)
    return persons


@pytest.fixture
def country():
    country = []
    for x in range(1, 11):
        u = Country.objects.create(name=str(x))
        country.append(u)
    return country


@pytest.fixture
def studio(country):
    count = 1
    studios = []
    for c in country:
        s = Studio.objects.create(country=c, name=str(count))
        count += 1
        studios.append(s)
    return studios


@pytest.fixture
def movies(studio, persons):
    movies = []
    for x in range(10):
        m = Movie.objects.create(title=str(x),year=x, directed_by=persons[x], studio=studio[x])
        m.actors.add(persons[x])
        movies.append(m)
    return movies

