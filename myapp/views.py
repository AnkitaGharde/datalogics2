from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')


def python(request):
    return render(request,'myapp/python.html')

def ML(request):
    return render(request,'myapp/ML.html')

def courses(request):
    return render(request,'myapp/courses.html')

def blog(request):
    return render(request,'myapp/blogs.html')

def contact(request):
        if request.method == 'POST':
            Name = request.POST['Name']
            Email = request.POST['Email']
            Message = request.POST['Message']
            Contact(Name=Name, Email=Email,Message=Message).save()
            return render(request, 'myapp/index.html')
        else:
            return render(request, 'myapp/contact.html')


def data(request):
    return render(request,'myapp/data_science.html')