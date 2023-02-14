from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('notes/',views.notes_view,name='notes'),
    path('notesdelete/<int:pk>',views.notesdelete_view,name='notesdelete'),
    path('notesdetails/<int:pk>',views.notes_detail,name='notesdetails'),
]
