from platform import uname

from django.shortcuts import render,redirect
from AdminApp.models import *
from WebApp.models import *
from django.contrib import messages
import razorpay



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
    uname = request.session.get('name')
    print("uname is ",uname)
    print("request :",request)
    if uname:
        cart_total = CartDbModel.objects.filter(UserName=uname).count()
    else:
        cart_total = 0

    starters =FoodDb.objects.filter(category_name='Starters')
    Course =FoodDb.objects.filter(category_name='Main_Course')
    Desserts=FoodDb.objects.filter(category_name='Desserts')
    Drinks=FoodDb.objects.filter(category_name='Drinks')



    context={

        'starters':starters,
        'Course':Course,
        'Desserts':Desserts,
        'Drinks':Drinks,
        'cart_total':cart_total,
    }
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')

def menu(request):
    menu = FoodDb.objects.all()
    uname = request.session.get('name')
    print("uname is ", uname)
    print("request :", request)
    if uname:
        cart_total = CartDbModel.objects.filter(UserName=uname).count()
    else:
        cart_total = 0

    starters =FoodDb.objects.filter(category_name='Starters')
    Course =FoodDb.objects.filter(category_name='Main_Course')
    Desserts=FoodDb.objects.filter(category_name='Desserts')
    Drinks=FoodDb.objects.filter(category_name='Drinks')


    context={

        'starters':starters,
        'Course':Course,
        'Desserts':Desserts,
        'Drinks':Drinks,
        'menu':menu,
        'cart_total':cart_total,
    }

    return render(request,'menu.html',context)

def add_cart(request):
    return render(request,'add_cart.html')

def save_cart_items(request):
    if request.method == "POST":
        print(request.POST.get("foodId"))
        print(request.POST.get("quantity"))
        print(request.POST.get("quantity"))

        food_id = request.POST.get("foodId")
        # quantity = request.POST.get("quantity")
        quantity = int(request.POST.get("quantity"))

        food = FoodDb.objects.get(id=food_id)
        total_price = food.price * quantity

        CartDbModel.objects.create(
            UserName=request.session.get("name"),
            food=food,
            Quantity=quantity,
            Total_Price=total_price
        )
    return redirect("menu")
def view_cart(request):
    if 'name' not in request.session:
        return redirect('loginpage')

    uname = request.session['name']
    cart_items = CartDbModel.objects.filter(UserName=uname)
    cart_total = CartDbModel.objects.filter(UserName=uname).count()
    grand_total = sum(item.Total_Price for item in cart_items)
    context = {
        "cart_items": cart_items,
        "grand_total": grand_total,
        'cart_total':cart_total,
    }

    return render(request,'view_cart_items.html',context)

def checkout(request):
    uname = request.session['name']
    cart_total = CartDbModel.objects.filter(UserName=uname).count()
    cart_items = CartDbModel.objects.filter(UserName=uname)

    total = 0
    for item in cart_items:
        total += item.Total_Price

    context = {
            'cart_total':cart_total,
            'cart_items':cart_items,
            'total':total,
    }
    return render(request,'checkout.html',context)


def payment(request):
    if request.method == "POST":

        request.session['name'] = request.POST.get('name')
        request.session['email'] = request.POST.get('email')
        request.session['phone'] = request.POST.get('phone')
        request.session['address'] = request.POST.get('address')
        request.session['payment'] = request.POST.get('payment')

        return render(request, 'payment.html')

    return redirect('checkout')

def payment_page(request):


    uname = request.session['name']
    print("Username:", uname)

    cart_total = CartDbModel.objects.filter(UserName=uname).count()

    cart_items = CartDbModel.objects.filter(UserName=uname)
    print("Items:", cart_items.count())



    total = 0

    for item in cart_items:
        total += item.Total_Price


    amount = total * 100  # Razorpay accepts paise
    price=int(total*100)
    print("Cart Total:", total)
    print("Razorpay Amount:", amount)

    print("Username:", uname)
    print("Items:", cart_items.count())
    print("Cart Total:", total)
    print("Razorpay Amount:", amount)


    payment = None

    if request.method == "POST":

        client = razorpay.Client(
            auth=(
                "rzp_test_0ib0jPwwZ7I1lT",
                "VjHNO5zKeKxz8PYe7VnzwxMR"
            )
        )


        payment = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1
        })


    return render(request,"payment.html",{"cart_total":cart_total,"pay_str":amount,"payment":payment})

def place_order(request):
    if request.method == "POST":

        uname = request.session.get("name")
        name = request.session.get("name")
        email = request.session.get("email")
        phone = request.session.get("phone")
        address = request.session.get("address")
        payment = request.session.get("payment")
        cart_items = CartDbModel.objects.filter(UserName=uname)

        for item in cart_items:
            OrderModel.objects.create(
                UserName=uname,
                Name=name,
                Food=item.food,
                Quantity=item.Quantity,
                Total_Price=item.Total_Price,
                Email=email,
                Phone=phone,
                Address=address,
                Payment=payment,
            )

        cart_items.delete()

        return redirect("home")

#
# def place_order(request):
#     if request.method == "POST":
#
#         uname = request.session.get("name")
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         address = request.POST.get("address")
#         payment = request.POST.get("payment")
#         print("Email is:",phone)
#
#         cart_items = CartDbModel.objects.filter(UserName=uname)
#         print(cart_items)
#
#         for item in cart_items:
#             OrderModel.objects.create(
#                 UserName=uname,
#                 Name=name,
#                 Food=item.food,
#                 Quantity=item.Quantity,
#                 Total_Price=item.Total_Price,
#                 Email=email,
#                 Phone=phone,
#                 Address=address,
#                 Payment=payment,
#             )
#
#         # Clear cart after order
#         cart_items.delete()
#
#         return redirect("home")
#


