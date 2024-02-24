from django.shortcuts import render

# Create your views here.


# Index File View

def IndexPage(request):
    return render(request,"app/index.html")
