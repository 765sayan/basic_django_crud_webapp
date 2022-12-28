from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form_object = StudentRegistration(request.POST)
        if form_object.is_valid():
            # form_object.save() #This saves the form info in the database
            name = form_object.cleaned_data['name']
            email = form_object.cleaned_data['email']
            password = form_object.cleaned_data['password']
            register_user = User(name=name, email=email, password=password)
            register_user.save() #This is another method for saving to database
            form_object = StudentRegistration()
    else:
        form_object = StudentRegistration()
    students_data_all = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': form_object, 'stu': students_data_all})


def edit_data(request, id):
    if request.method == 'POST':
        user_data = User.objects.get(pk=id)
        form_object = StudentRegistration(request.POST, instance=user_data) #The data from the user_data object coming from database will be entered in the form object
        if form_object.is_valid():
            form_object.save()

    else:
        user_data = User.objects.get(pk=id)
        form_object = StudentRegistration(instance=user_data)
    return render(request, 'enroll/updatestudent.html', {'form': form_object})


def delete_data(request, id):
    if request.method == 'POST':
        user_data = User.objects.get(pk=id)
        user_data.delete() #This will delete data from database
        return HttpResponseRedirect('/') # '/' this means the page will be redirected to same page