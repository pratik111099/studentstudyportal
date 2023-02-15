from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('notes/',views.notes_view,name='notes'),
    path('notesdelete/<int:pk>',views.notesdelete_view,name='notesdelete'),
    path('notesdetails/<int:pk>',views.notes_detail,name='notesdetails'),
    path('homework/',views.homework_view,name='homework'),
    path('updatehomework/<int:pk>',views.updatehomework,name='updatehomework'),
    path('deletehomework/<int:pk>',views.deletehomework,name='deletehomework'),
]
