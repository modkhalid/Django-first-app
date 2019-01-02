from django.shortcuts import render

from myapp.forms import UserFormBasic,UserInfoForm


from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'myapp/index.html',{'title':"welcome to index Page"})

def home(request):
    return render(request,'myapp/index.html',{'title':"welcome to Home Page"})

def registration(request):

    registered=False
    if request.method=='POST':
        user_form=UserFormBasic(request.POST)
        profile_form=UserInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
                # print("yes it is ",profile.profile_pic)
            # print(request.FILES)

            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserFormBasic()
        profile_form=UserInfoForm()

    return render(request,'myapp/register.html',{'registered':registered,'user':user_form,'profile':profile_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('hi you are Login')


def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        # getauthenticate
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('USER IS NOT ACTIVE ')
            # return HttpResponseRedirect(reverse('index'))
        else:
            print('User tried {} and password {}'.format(username,password))
    else:
        return render(request,'myapp/login.html',{})
