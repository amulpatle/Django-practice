from django.shortcuts import render
from .models import *
# Create your views here.


# Index File View

def IndexPage(request):
    return render(request,"app/index.html")

def UploadImage(request):
    if request.method == "POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']
        
        newimg = ImageData.objects.create(Imagename=imagename,Image = pics)
        return render(request,"app/show.html")
    