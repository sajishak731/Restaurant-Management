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

def contact_page(request):
    return render(request,'Contacts_page.html')

def Send_message(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        print("MEssage")
        messages.success(request, "Your message has been sent successfully.")
        return redirect('home')

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


# def payment(request):
#     if request.method == "POST":
#
#         request.session['name'] = request.POST.get('name')
#         request.session['email'] = request.POST.get('email')
#         request.session['phone'] = request.POST.get('phone')
#         request.session['address'] = request.POST.get('address')
#         request.session['payment'] = request.POST.get('payment')
#
#         payment_method = request.POST.get("payment")
#         if payment_method == "Cash on Delivery":
#             return redirect(place_order) # Skip Razorpay
#         else:
#             return redirect(payment_page)      # Go to Razorpay
#
#
#
#     return redirect('checkout')

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

# def place_order(request):
#     if request.method == "POST":
#
#         uname = request.session.get("name")
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         address = request.POST.get("address")
#         payment = request.POST.get("payment")
#
#         cart_items = CartDbModel.objects.filter(UserName=uname)
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
#                 Payment=payment
#             )
#
#         cart_items.delete()
#
#         return redirect("home")
def book_table(request):

    tables = TableDB.objects.filter(active="Yes")
    print("Table ID:", request.POST.get("table"))
    print(TableDB.objects.all())

    if request.method == "POST":

        customer_name = request.POST.get("customer_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        guests = request.POST.get("guests")
        table_id = request.POST.get("table")

        # Check whether table already booked
        already_booked = BookingDB.objects.filter(
            table_id=table_id,
            booking_date=booking_date,
            booking_time=booking_time,
            status="Booked"
        ).exists()

        if already_booked:
            return render(request, "book_table.html", {
                "tables": tables,
                "error": "Selected table is already booked."
            })

        BookingDB.objects.create(
            customer_name=customer_name,
            phone=phone,
            email=email,
            booking_date=booking_date,
            booking_time=booking_time,
            guests=guests,
            table_id=table_id
        )

        return redirect("booking_success")

    return render(request, "book_table.html", {"tables": tables})

def booking_success(request):
    return render(request, "book_table_success.html")
def payment_success(request):
    return render(request,'Payment.success.html')

def payment(request):
    if request.method == "POST":

        request.session['name'] = request.POST.get('name')
        request.session['email'] = request.POST.get('email')
        request.session['phone'] = request.POST.get('phone')
        request.session['address'] = request.POST.get('address')
        request.session['payment'] = request.POST.get('payment')

        payment_method = request.POST.get("payment")

        if payment_method == "Cash on Delivery":
            return redirect("place_order")
        else:
            return redirect("payment_page")

    return redirect("checkout")

# def place_order(request):
#
#     uname = request.session.get("name")
#     name = request.session.get("name")
#     email = request.session.get("email")
#     phone = request.session.get("phone")
#     address = request.session.get("address")
#     payment = request.session.get("payment")
#
#     cart_items = CartDbModel.objects.filter(UserName=uname)
#
#     for item in cart_items:
#         OrderModel.objects.create(
#             UserName=uname,
#             Name=name,
#             Food=item.food,
#             Quantity=item.Quantity,
#             Total_Price=item.Total_Price,
#             Email=email,
#             Phone=phone,
#             Address=address,
#             Payment=payment
#         )
#
#     cart_items.delete()
#
#     return redirect("home")

def place_order(request):

    uname = request.session.get("name")
    name = request.session.get("name")
    email = request.session.get("email")
    phone = request.session.get("phone")
    address = request.session.get("address")
    payment = request.session.get("payment")


    cart_items = CartDbModel.objects.filter(UserName=uname)

    grand_total = sum(item.Total_Price for item in cart_items)

    # Create one order
    order = OrderModel.objects.create(
        UserName=uname,
        Name=name,
        Email=email,
        Phone=phone,
        Address=address,
        Payment=payment,
        Grand_Total=grand_total
    )

    # Create one order item for each cart item
    for item in cart_items:
        OrderItem.objects.create(
            Order=order,
            Food=item.food,
            Quantity=item.Quantity,
            Total_Price=item.Total_Price
        )

    cart_items.delete()

    return redirect("payment_success")



def my_orders(request):
    uname=request.session.get('name')
    print("name is ::::::::::",uname)
    orders = OrderModel.objects.filter(UserName="sajisha")
    print(orders)

    return render(request,'My_orders.html',{'orders':orders})




#book_table success and payment success to design
































































































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


