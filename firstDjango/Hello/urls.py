from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('<str:name>', views.greet, name='greet'),
    path('rin',views.rin, name='rin'),
    path('estrea',views.estrea, name='estrea')
]