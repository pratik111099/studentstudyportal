from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Notes,Homework, ToDo
from .forms import NotesForm, HomeworkForm, SearchForm, TempConversionForm, ToDoForm, MassConversionForm
from django. contrib import messages
from youtubesearchpython import VideosSearch
import requests
import wikipedia
from decimal import Decimal
from .utils import convert
from django.contrib.auth.decorators import login_required

# Create your views here.
# Notes View  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def home_view(request):
    return render(request,'dashboard/home.html')

@login_required
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

@login_required
def notesdelete_view(request,pk=None):
    note=Notes.objects.get(id=pk).delete()
    messages.warning(request,'Note Deleted')
    return redirect('notes')

@login_required
def notes_detail(request,pk):
    note=Notes.objects.get(id=pk)
    context={
        'note':note
    }
    return render(request,'dashboard/notes_detail.html',context)




# HomeWork View !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
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


@login_required
def updatehomework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finish == True:
        homework.is_finish = False
    else:
        homework.is_finish = True

    homework.save()
    return redirect('homework')

@login_required
def deletehomework(request,pk=None):
    home=Homework.objects.get(id=pk).delete()
    messages.success(request,'Homework deleted successfully')
    return redirect('homework')


# Youtube View   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
def youtube_view(request):
    if request.method == "POST":
        form=SearchForm(request.POST)
        text=request.POST['text']
        video=VideosSearch(text,limit=10)
        result_list = []
        for v in video.result()['result']:
            dict={
                'input':text,
                'title':v['title'],
                'duration':v['duration'],
                'thumbnail':v['thumbnails'][0]['url'],
                'channel':v['channel']['name'],
                'link':v['link'],
                'views':v['viewCount']['short'],
                'published':v['publishedTime'],
            }
           
            desc=''
            if v['descriptionSnippet']:
                for j in v['descriptionSnippet']:
                    desc += j['text']
            dict['description'] = desc
            result_list.append(dict)
            print(result_list)
            print('\n\n\n\n\n')
            context={
                'form':form,
                'result_list':result_list
            }
        return render(request,'dashboard/youtube.html',context)

    else:
        form = SearchForm()
    context={
        'form':form
    }
    return render(request,'dashboard/youtube.html',context)


# To DO View   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
def Todo_view(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['status']
                if finished == 'on':
                    status_input = True
                else:
                    status_input = False
            except:
                status_input = False
        todo = ToDo(user=request.user,
                         title=request.POST['title'],
                         status=status_input
                         )
        todo.save()
        return redirect('todo')
        
    else:
        form = ToDoForm()

    todo=ToDo.objects.filter(user=request.user)
    completed=True
    for t in todo:
        if t.status == False:
            completed=False

    context={
        'todo':todo,
        'form':form,
        'completed':completed,
    }
    return render(request,'dashboard/todo.html',context)

@login_required
def StatusToDO(request,pk):
    todo=ToDo.objects.get(id=pk)
    if todo.status == True:
        todo.status = False
    else:
        todo.status = True
    todo.save()
    return redirect('todo')

@login_required
def DeleteToDO(request,pk):
    delete=ToDo.objects.get(id=pk).delete()
    return redirect('todo')



# Books View   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
def Books_view(request):
    if request.method == "POST":
        form=SearchForm(request.POST)
        text=request.POST['text']
        url="https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        ans = r.json()
        result_list = []

        for i in range(10):
            result_dict={
                'title':ans['items'][i]['volumeInfo']['title'],
                'subtitle':ans['items'][i]['volumeInfo'].get('subtitle'),
                'description':ans['items'][i]['volumeInfo'].get('description'),
                'count':ans['items'][i]['volumeInfo'].get('pageCount'),
                'categories':ans['items'][i]['volumeInfo'].get('categories'),
                'rating':ans['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':ans['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':ans['items'][i]['volumeInfo'].get('previewLink'),
            }
            result_list.append(result_dict)
        print(result_list)
        context={
        'form':form,
        'result_list':result_list
        }
        return render(request,'dashboard/books.html',context)

    else:
        form=SearchForm()
    context={
        'form':form
    }
    return render(request,'dashboard/books.html',context)




# Dictionary View    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
def Dictionary_view(request):
    if request.method == "POST":
        form=SearchForm(request.POST)
        text=request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        aws = r.json()
        
        try: 
            phonetics = aws[0]['phonetics'][0]['text']
            audio = aws[0]['phonetics'][0]['audio']
            definition = aws[0]['meanings'][0]['definitions'][0]['definition']
            example =aws[0]['meanings'][0]['definitions'][0]['example']
            
            
            context={
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
            }
         
        
           
        except:
            context={
                'form':form,
                'input':''
            }
        return render(request,'dashboard/dictionary.html',context)
           
    else:
        form = SearchForm()

    context = {
        'form':form,
    }
    return render(request,'dashboard/dictionary.html',context)






# wikipedia View    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
def wikipedia_search(request):
    if request.method == "POST":
        form=SearchForm(request.POST)
        search_term = request.POST['text'] 
        search_results = wikipedia.search(search_term)
        context={
            'form':form,
            'search_results':search_results
        }
        return render(request, 'dashboard/wiki.html', context)
    
    form=SearchForm()

    context={
        'form':form
    }
    return render(request, 'dashboard/wiki.html', context)


@login_required
def wikilistSearch(request,query):
    try:
        page = wikipedia.page(query)
        print(page.url)
        if page:
            context = {
                'title': page.title,
                'content': page.content,
                'url': page.url
            }
            return render(request,'dashboard/wiki.html',context)

    except:
        return HttpResponse("Sorry imformation not available please try other link!!!!!!!!!!!")







# Conversion View    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# @login_required
# def conversion_view(request,):
#     return render(request, 'dashboard/conversion.html')
   

@login_required
def mass_conversion_view(request):
    if request.method == 'POST':
        form = MassConversionForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            converted_value = convert(value,from_unit,to_unit)
          
            if converted_value == -1:
                return HttpResponse('<h1>conversion not avaliable</h1>')
            
            print(value)
            return render(request, 'dashboard/conversion.html', {
                'value': value,
                'from_unit': from_unit,
                'to_unit': to_unit,
                'converted_value':converted_value
            })
    else:
        form = MassConversionForm()
    return render(request, 'dashboard/conversion.html', {'form': form})


@login_required
def temp_conversion_view(request):
    print(id)
    if request.method == 'POST':
        form = TempConversionForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            converted_value = convert(value,from_unit,to_unit)
          
            if converted_value == -1:
                return HttpResponse('<h1>conversion not avaliable</h1>')
            
            print(value)
            return render(request, 'dashboard/conversion.html', {
                'value': value,
                'from_unit': from_unit,
                'to_unit': to_unit,
                'converted_value':converted_value
            })
    else:
        form = TempConversionForm()
    return render(request, 'dashboard/conversion.html', {'form': form})