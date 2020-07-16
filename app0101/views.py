from django.shortcuts import render,redirect
from django.contrib import messages
from app0101.forms import shedule_classess,user_register_form
from app0101.models import new_shedule_class_model,user_register

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
    formss = shedule_classess
    return render(request, 'update_shedule_classes.html', {'data':dta,'sforms':formss})


def update_shedule_classes_successf(request):
    idn = request.POST.get('u')
    c_name = request.POST.get('u0')
    fname = request.POST.get('u1')
    datee = request.POST.get('u2')
    timeee = request.POST.get('u3')
    feee = request.POST.get('u4')
    duration_d = request.POST.get('u5')
    new_shedule_class_model.objects.filter(idno=idn).update(faculty_name=fname,date=datee,time=timeee,fee=feee,durtion_days=duration_d)
    return redirect('view_all_shedule_classes')


def Delete_Shedule_class(request):
    idn = request.GET.get('Deleteidno')
    new_shedule_class_model.objects.get(idno=idn).delete()
    messages.success(request, 'deleted')
    return view_all_shedule_classes(request)


def view_all_shedule_classes_Enduser(request):
    records = new_shedule_class_model.objects.all()
    return render(request, 'user/view_all_shedule_classes_Enduser.html',{'show':records})


def register_user(request):
    form = user_register_form
    return render(request, 'user/register_user.html', {'register_form':form})


def regiser_user_success(request):
    usr_register_form = user_register_form(request.POST)
    if usr_register_form.is_valid():
        usr_register_form.save()
        return render(request, 'user/register_user.html',{'register_form':user_register_form,'mes':'register sucessfully'})
    else:
        return render(request,'user/register_user.html',{'register_form':usr_register_form,'mes':'register unsuccessfull'})


def view_all_registerd_users(request):
    register_users = user_register.objects.all()
    return render(request, 'view_all_registerd_users.html', {'users':register_users})


def user_search(request):
    course_id = request.GET.get('sea')
    course_details = new_shedule_class_model.objects.filter(idno=course_id)
    return render(request, 'user/user_search.html',{'data':course_details})


def search_users(request):
    idn = request.POST.get('s1')
    dat = user_register.objects.filter(Idno=idn)
    if dat:
        users = user_register.objects.all()
        return render(request, 'view_all_registerd_users.html', {'data':dat,'users':users})
    else:
        users = user_register.objects.all()
        return render(request, 'view_all_registerd_users.html', {'imes':"Invalid Id Number",'users':users})


def delete_user(request):
    idnu = request.GET.get('idnoo')
    user_register.objects.get(Idno=idnu).delete()
    return search_users(request)


def user_log_in(request):
    return render(request, 'user/user_log_in.html')