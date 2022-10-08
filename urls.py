from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('show', views.show, name='show'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('fetch', views.fetch, name='fetch'),
    path('sign1', views.sign1, name='sign1'),
    path('login', views.login, name='login'),
    path('showData', views.showData, name='showData'),
    path('newadd', views.newadd, name='newadd'),
    path('fetchrep', views.fetchrep, name='fetchrep'),
    path('fetchcity', views.fetchcity, name='fetchcity'),
    path('', views.todos, name='todos'),
    path('delete/<int:id>', views.delete, name='delete'),















]
