from django.shortcuts import render,redirect
from AdminApp.models import CategoryDb, FoodDb
from WebApp.models import *
from django.contrib import messages



# Create your views here.
def loginpage(request):
    return render(request,'LoginPage.html',)


def user_sign_up(request):
    if request.method == "POST":
        name =request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        con_password = request.POST.get('cpswd')
        obj =RegistrationDb(name=name,email=email,password=password,confirm_password=con_password)
        if RegistrationDb.objects.filter(name=name).exists():
            print("username already existing....!")
            return redirect(home)

        elif RegistrationDb.objects.filter(email=email).exists():
            print("email already existing..!")
            return redirect(loginpage)
        else:
            obj.save()
            return redirect(home)
def user_sign_in(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        if RegistrationDb.objects.filter(name=name,password=pswd).exists():
             request.session['name']=name
             request.session['password'] =pswd
             return redirect(home)
        else:
            print("username already exists")
            return redirect(user_sign_in)
    else:
        print("invalid username")
        return redirect(loginpage)

def user_logout(request):
    del request.session["name"]
    del request.session["password"]
    messages.warning(request, "Logout succesfully....!")
    return redirect(loginpage)

def home(request):
    menu = FoodDb.objects.all()
    starters =FoodDb.objects.filter(category_name='Starters')
    Course =FoodDb.objects.filter(category_name='Main_Course')
    Desserts=FoodDb.objects.filter(category_name='Desserts')
    Drinks=FoodDb.objects.filter(category_name='Drinks')

    print(Course)
    print(Course.count())

    for i in FoodDb.objects.all():
        print(repr(i.category_name))
    context={

        'starters':starters,
        'Course':Course,
        'Desserts':Desserts,
        'Drinks':Drinks
    }
    return render(request,'home.html',context)

def menu(request):
    menu = FoodDb.objects.all()
    starters =FoodDb.objects.filter(category_name='Starters')
    Course =FoodDb.objects.filter(category_name='Main_Course')
    Desserts=FoodDb.objects.filter(category_name='Desserts')
    Drinks=FoodDb.objects.filter(category_name='Drinks')

    print(Course)
    print(Course.count())

    for i in FoodDb.objects.all():
        print(repr(i.category_name))
    context={

        'starters':starters,
        'Course':Course,
        'Desserts':Desserts,
        'Drinks':Drinks,
        'menu':menu,
    }

    return render(request,'menu.html',context)

def add_cart(request):
    return render(request,'add_cart.html')