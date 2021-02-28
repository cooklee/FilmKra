from django.test import TestCase
import pytest
# Create your tests here.
from django.urls import reverse


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
def test_movie_list(client):
    response = client.get(reverse('movie_list'))
    assert response.status_code == 200