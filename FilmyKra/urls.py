"""FilmyKra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from filmweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('persons/', views.PersonListView.as_view(), name='person_list'),
    path('movies/', views.movie_view, name='movie_list'),
    path('add_person/', views.add_person_view, name='add_person'),
    path('add_movie/', views.add_movie_view, name='add_movie'),
    path('person/<int:id>/', views.detail_person_view, name='person'),
    path('movie/<int:id>/', views.detail_movie_view, name='movie'),
    path('movies_by_studio/<int:id>/<int:year>/<str:title>/', views.StudioMovieView.as_view(), name='movie2'),
    path('session/', views.add_info_to_session, name='session'),
    path('cookie/', views.add_cookie, name='cookie'),
    path('country/', views.CountryView.as_view(), name='country_list'),
    path('add_country/', views.AddCountryView.as_view(), name='add_country'),
    path('add_studio/', views.AddStudioView.as_view(), name='add_studio'),
    path('studios/', views.StudioListView.as_view(), name='studio_list'),
    path('studio/<int:id>/', views.StudioDetailView.as_view(), name='studio_detail'),
    path('list_users/', views.ListUserView.as_view(), name='list_user'),
    path('login/', views.LoginView.as_view(), name='login')
]

