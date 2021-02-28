import pytest
from django.test import Client
from django.contrib.auth.models import User

from filmweb.models import Person


@pytest.fixture
def client():
    c = Client()
    return c

@pytest.fixture
def users():
    users = []
    for x in range(1,11):
        u = User.objects.create(username=str(x))
        users.append(u)
    return users


@pytest.fixture
def persons():
    persons = []
    for x in range(1,11):
        u = Person.objects.create(first_name=str(x), last_name='dudek')
        persons.append(u)
    return persons