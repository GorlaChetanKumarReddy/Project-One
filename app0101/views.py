from django.shortcuts import render,redirect
from django.contrib import messages
from app0101.forms import shedule_classess

# Create your views here.
def showIndex(request):
    return render(request, 'index.html')


def admin_log_in(request):
    uname = request.POST.get('a1')
    passw = request.POST.get('a2')
    if uname == 'admin':
        if passw == 'admin1':
            return render(request, 'admin_log_in_sucess.html')
        messages.error(request, 'wrong password')
        return redirect('main')
    messages.error(request, 'wrong username')
    return redirect('main')


def shedule_new_classes(request):
    formm = shedule_classess
    return render(request, 'shedule_new_classes.html' ,{'shedule_new_class_form':formm})


def new_shedule_classes_added(request):
    formmm = shedule_classess(request.POST)
    if formmm.is_valid():
        formmm.save()
        messages.success(request, 'new class add sucessfully')
    return redirect('shedule_new_classes')