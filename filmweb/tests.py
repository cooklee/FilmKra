from django.test import TestCase
import pytest
# Create your tests here.
from django.urls import reverse

from filmweb.models import Person, Studio


def test_check_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_person_list(client, persons):
    response = client.get(reverse('person_list'))
    assert response.status_code == 200
    persons_from_view = response.context['object_list']
    assert persons_from_view.count() == len(persons)
    for x in persons_from_view:
        assert x in persons


@pytest.mark.django_db
def test_add_person(client):
    first_name = 'slawek'
    last_name = 'bo'
    assert Person.objects.all().count() == 0
    client.post(reverse("add_person"), {'first_name': first_name,
                                        "last_name": last_name})
    assert Person.objects.all().count() == 1
    Person.objects.get(first_name=first_name, last_name=last_name)


@pytest.mark.django_db
def test_studio_list_user_login(client, studio, users):
    client.force_login(users[0])
    response = client.get(reverse('studio_list'))
    assert response.status_code == 200
    studio_from_view = response.context['object_list']
    assert studio_from_view.count() == len(studio)
    for x in studio_from_view:
        assert x in studio


@pytest.mark.django_db
def test_studio_list_user_not_login(client):
    response = client.get(reverse('studio_list'))
    assert response.status_code == 302
    path = response.url.split('?')[0]
    next = response.url.split('?')[1]
    assert path == reverse('login')
    assert next == 'next=/studios/'


@pytest.mark.django_db
def test_movie_list(client, movies):
    response = client.get(reverse('movie_list'))
    assert response.status_code == 200
    movie_from_view = response.context['object_list']
    assert movie_from_view.count() == len(movies)
    for item in movie_from_view:
        assert item in movies


@pytest.mark.django_db
def test_add_studio(client, country):
    nazwa = 'std1'
    country_id = country[0].id
    response = client.post(reverse('add_studio'), {'nazwa': nazwa,
                                                   "country": country_id})

    assert response.status_code == 302
    Studio.objects.get(name=nazwa, country=country[0])
    assert response.url == reverse('studio_list')
