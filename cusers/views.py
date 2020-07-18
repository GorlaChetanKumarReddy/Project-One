from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def cusers_register(request):
    return render(request, 'cusers/cusers_register.html')




def cuser_log_in(request):
    return render(request,'cusers/cuser_log_in.html')



def cusers_register_request(request):
    if request.method == "POST":
        name = request.POST['cu1']
        l_name = request.POST['cu2']
        user_nme = request.POST['cu3']
        email_id = request.POST['cu4']
        Pwd = request.POST['cu5']
        Pwd2 = request.POST['cu6']
        Phone = request.POST['cu7']
        if Pwd == Pwd2:
            if User.objects.filter(username=user_nme).exists():
                messages.error(request,'user name is alredy exists try with another username')
                return  redirect('cusers_register')
            elif User.objects.filter(email=email_id).exists():
                messages.error(request, 'email is alredy exists try with another email')
                return redirect('cusers_register')
            else:
                users = User.objects.create_user(first_name=name,username=user_nme,email=email_id,password=Pwd,last_name=l_name)
                users.save();
                messages.success(request, 'register successfully')
                return redirect('cuser_log_in')
        else:
            messages.error(request, 'password and confirm-password does not match')
            return redirect('cusers_register')
    return redirect('cuser_log_in')


def cuser_loin_request(request):
    if request.method == "POST":
        usern = request.POST["cul1"]
        paswd = request.POST["cul2"]
        user = auth.authenticate(username=usern,password=paswd)
        if user is not None:
            auth.login(request,user)
            return redirect('main')
        else:
            messages.error(request, 'invalid credensials')
            return redirect('cuser_log_in')
    return render(request,'user/user_log_in.html')