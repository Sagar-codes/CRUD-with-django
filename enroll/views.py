from enroll.models import Todo
from django.shortcuts import render, HttpResponseRedirect
from .forms import TodoForm


# Create your views here.

#This Function will Show the item In the index page
def index(request):
    todolist = Todo.objects.all() # to show data from database  to user
    return render(request, 'enroll/index.html', {'todolist':todolist})

#This Function will add new item in database
def add(request):
    if request.method == 'POST': # if request is post
        fm = TodoForm(request.POST) # collect the data in a variable if the data is in post method
        if fm.is_valid(): #checking if the data is valid or not if its true
            tit = fm.cleaned_data['title'] 
            des = fm.cleaned_data['desc']
            #This is for save the cleaned data into database
            reg = Todo(title=tit, desc=des) # then save the data in cleaned_data variable.
            reg.save() # Saving the data 
            fm = TodoForm() # It is to clear form after submitting the data into database
            # todolist = Todo.objects.all.get() # to show data from database  to user
    else:
        fm = TodoForm() # it will return a blank form after submitting
        
    return render(request, 'enroll/add.html', {'form': fm})


#this function will update the Data in Database
def update_data(request, id):
    if request.method == 'POST': # if request method is post then 
        pi = Todo.objects.get(pk=id) # Collect the id in a variable if the data is in post method
        fm = TodoForm(request.POST, instance=pi) # take it back to the model instance
        if fm.is_valid(): #checking if the form is valid (if it contains data or not)
            fm.save() # saving form
    else:
        pi = Todo.objects.get(pk=id) # else collect the id from the database
        fm = TodoForm(instance=pi) # save it back to instance of model

    return render(request,'enroll/updatetodo.html', {'form':fm})


#This function will Delete The data from index page
def remove_data(request, id):
    if request.method == 'POST': #if  request method is post.
        rd = Todo.objects.get(pk=id) #get the id of the todolist  (pk means primary key)
        rd.delete() # then delete the data using delete function
        return HttpResponseRedirect('/') # and return the home page by redirecting.
