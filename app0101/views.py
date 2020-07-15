from django.shortcuts import render,redirect
from django.contrib import messages
from app0101.forms import shedule_classess
from app0101.models import new_shedule_class_model

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


def view_all_shedule_classes(request):
    context = new_shedule_class_model.objects.all()
    return render(request, 'view_all_shedule_classes.html', {'show_all_classess':context})


def update_shedule_classes(request):
    iddata = request.GET.get('upda')
    dta = new_shedule_class_model.objects.get(idno=iddata)
    return render(request, 'update_shedule_classes.html', {'data':dta})