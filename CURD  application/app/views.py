from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    # Data come from HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    # Creating Object of Model Class
    # Inserting Data into Table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    # After Insert render on Show.html
    # return render(request,"app/show.html")
    return redirect('showpage')

def ShowPage(request):
    all_data = Student.objects.all()#for fatching all the data
    return render(request,"app/show.html",{'key1':all_data})

#Edit page View
def EditPage(request,pk):
    # fetching the data of particular ID
    get_data = Student.objects.get(id = pk)
    return render(request,"app/edit.html",{'key2':get_data})


def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    
    #query for update
    
    udata.save()
    
    #render to show page
    
    return redirect('showpage')
    

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    #Query for Delete
    ddata.delete()
    return redirect('showpage')