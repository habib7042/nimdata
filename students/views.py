from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def students(request):
    data = Student.objects.all().values()
    return render(request, 'students.html', {"data": data})

def result(request,id):
    data = Student.objects.get(id=id)
    return render(request, 'result.html', {"data": data})