from django.urls import path

from . import views as v


app_name = 'todo'
urlpatterns = [
    path('', v.index, name='index'),
    path('new/', v.new, name='new'),
]