from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from signup.models import Employee, Student_Data, Reporter_add,City,Task
 
def home(request):
    return render(request, 'index.html', {'link': 'http://127.0.0.1:8000/'})


def about(request):
    return HttpResponse("<h1>I m about world!</h1>")


def service(request):
    return HttpResponse("<h1>I m Service Page!</h1>")


def show(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        courses = request.POST['Courses']

        student = Student_Data(
            first_name=firstname,
            last_name=lastname,
            Email_id=email,
            Courses=courses,
        )
        student.save()
        return HttpResponse("<h1><center>Data saved succesfully</center></h1>")
    else:
        return HttpResponse('<h1>hello plz try again</h1>')


def fetch(request):
    alldata = Student_Data.objects.all()
    return render(request, 'hello.html', {'data': alldata})


def sign1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        employee = Employee(
            email=email,
            password=password

        )
        employee.save()
        return render(request, "login.html")
    else:
        return render(request, "signsup.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        employee = Employee.objects.get(email=email)
        print(email)

        if employee.password == request.POST['pass']:
            return render(request, 'show.html')
    
        return HttpResponse("<h1>Incorrect Password</h1>")
    return render(request, 'login.html')

    
def showData(request):
    alldata = Employee.objects.all()
    return render(request, 'show.html', {'data': alldata})


def newadd(request):
     if request.method == 'POST':
        name = request.POST['name']
        job = request.POST['job']
        city = request.POST['city']
        if(True):
            reporter_add = Reporter_add(
            name = name,
            job=job,
            city=city,
        )
        reporter_add.save()
        return HttpResponse("<h1><center>Data saved succesfully</center></h1>")
     else:
        return render(request, 'empadd.html')


def fetchrep(request):
    if request.method == 'POST':
        city = request.POST['city']
        data=Reporter_add.objects.filter(city=city)
        return render(request, 'reports.html', {'data': data})
    else:
        return render(request, 'reports.html')


def fetchcity(request):
    alldata = City.objects.all()
    return render(request, 'showcity.html', {'data': alldata})







def todos(request):
 alldata = Task.objects.all()
 if request.method == 'POST':
            task = Task(
                Task_title=request.POST['title'],
                Description = request.POST['tarea']
                )
            task.save()
            return redirect('/')
 return render(request, 'todo.html', {'data': alldata})
 

def delete(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return redirect('/')











