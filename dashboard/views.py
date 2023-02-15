from django.shortcuts import redirect, render
from .models import Notes,Homework
from .forms import NotesForm, HomeworkForm
from django. contrib import messages

# Create your views here.
# Notes View  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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




# HomeWork View !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def homework_view(request):
    if request.method =="POST":
        form=HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finish']
                if finished == 'on':
                    finished = True
                else:
                    finished = False

            except:
                finished=False
            homework=Homework(
                                user=request.user,
                                subject=request.POST['subject'],
                                title=request.POST['title'],
                                descriptions=request.POST['descriptions'],
                                due=request.POST['due'],
                                is_finish=finished)
            homework.save()
            messages.success(request,'Homework is submited successfully')
            return redirect('homework')
        else:
           pass
           
            

    else:
        form=HomeworkForm()

    homework=Homework.objects.filter(user=request.user)
    homework_done=True
    for h in homework:
        if h.is_finish == False:
            homework_done=False
            
    context={
        'form':form,
        'homework':homework,
        'homework_done':homework_done
    }
    return render(request,'dashboard/homework.html',context)



def updatehomework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finish == True:
        homework.is_finish = False
    else:
        homework.is_finish = True

    homework.save()
    return redirect('homework')

def deletehomework(request,pk=None):
    home=Homework.objects.get(id=pk).delete()
    messages.success(request,'Homework deleted successfully')
    return redirect('homework')


