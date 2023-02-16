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

    path('youtube/',views.youtube_view,name='youtube'),

    path('todo/',views.Todo_view,name='todo'),
    path('statustodo/<int:pk>',views.StatusToDO,name='statustodo'),
    path('deletetodo/<int:pk>',views.DeleteToDO,name='deletetodo'),
    
    path('books/',views.Books_view,name='books'),
    
    path('dictionary/',views.Dictionary_view,name='dictionary'),
    
    path('wikipedia/',views.wikipedia_search,name='wikipedia'),
    path('wikipediasearch/<str:query>/',views.wikilistSearch,name='wikipediasearch'),
    
    path('conversion/',views.conversion_view,name='conversion'),    
    path('conversionm/',views.mass_conversion_view,name='conversionm'),    
    path('conversiont/',views.temp_conversion_view,name='conversiont'),    
  
]
