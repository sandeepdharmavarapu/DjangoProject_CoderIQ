from django.conf.urls import  include, url
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [url('index',views.index, name='index'),
		url('problem1',csrf_exempt(views.problem1), name='problem1'),
		url('problem2',views.problem2, name='problem2'),
		url('problem3',views.problem3, name='problem3')]
