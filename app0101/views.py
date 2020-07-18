from django.shortcuts import render,redirect
from django.contrib import messages
from app0101.forms import shedule_classess,user_register_form
from app0101.models import new_shedule_class_model,user_register
from django.db.models import Q

# Create your views here.
def showIndex(request):
    return render(request, 'index.html')


def admin_log_in(request):
    uname = request.POST.get('a1')
    passw = request.POST.get('a2')
    if uname == 'admin':
        if passw == '123456':
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
    course_name = request.POST.get('sea1','')
    if course_name:
        course_details = new_shedule_class_model.objects.filter(Q(name__icontains=course_name) |
                                                                Q(faculty_name__icontains=course_name) |
                                                                Q(date__icontains=course_name))
        return render(request, 'user/user_search.html', {'data': course_details,'searchname':course_name})
    else:
        return render(request,'view_all_shedule_classes.html',{"messag":course_name})


def search_users(request):
    idn = request.POST.get('s1')
    dat = user_register.objects.filter(Idno=idn)
    if dat:
        users = user_register.objects.all()
        return render(request, 'view_all_registerd_users.html', {'data':dat,'users':users})
    else:
        users = user_register.objects.all()
        return render(request, 'view_all_shedule_classes.html', {'imes':"Invalid Id Number",'show':users})


def delete_user(request):
    idnu = request.GET.get('idnoo')
    user_register.objects.get(Idno=idnu).delete()
    return search_users(request)


def user_log_in(request):
    return render(request, 'user/user_log_in.html')


def user_log_in_sucess(request):
    uname = request.POST.get('ul1')
    upas = request.POST.get('ul2')
    usr = user_register.objects.filter(Contact_No=uname)
    if usr:
        upasswo = user_register.objects.filter(Password=upas)
        if upasswo:
            profiledetails = user_register.objects.all()
            return render(request,'index.html',{'uname':uname,"userprofile":profiledetails})
        else:
            return render(request, 'user/user_log_in.html',{'umes':"wrong password"})
    else:
        return render(request,'user/user_log_in.html', {'umes':"wrong phone number"})


def admin_log_inpage(request):
    return render(request,'index.html',{"log":"lo"})