from django.shortcuts import redirect, render
from .models import Notes
from .forms import NotesForm
from django. contrib import messages

# Create your views here.
def home_view(request):
    return render(request,'dashboard/home.html')

def notes_view(request):
    notes=Notes.objects.filter(user=request.user)

    if request.method=="POST":
        form=NotesForm(request.POST)
        if form.is_valid:
            note=Notes(user=request.user, title=request.POST['title'], decriptions=request.POST['decriptions'])
            note.save()
        messages.success(request,'Notes Added Successfully')

    else:
        form=NotesForm()
    context={
        'notes':notes,
        'form':form
    }
    return render(request,'dashboard/notes.html',context)

def notesdelete_view(request,pk=None):
    note=Notes.objects.get(id=pk).delete()
    messages.warning(request,'Note Deleted')
    return redirect('notes')

def notes_detail(request,pk):
    note=Notes.objects.get(id=pk)
    context={
        'note':note
    }
    return render(request,'dashboard/notes_detail.html',context)