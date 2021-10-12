from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
        



    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']

        if p1 == p2:
            if User.objects.filter(username=username).exists():
                # print('username taken')
                messages.info(request, 'username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=p1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'user created')
                return redirect('login')

        else:
            print('not matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')