from django.shortcuts import render,redirect,get_object_or_404
from AdminApp.models import CategoryDb, FoodDb, StaffDb, TableDB
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from WebApp.models import *


# Create your views here.
def loginpage(request):
    return render(request,'login.html')


def dashboard(request):
    return render(request,'dashboard.html')
def Categories_Add(request):
    return render(request,'Categories_Add.html')

def Category_Save(request):
    if request.method == "POST":
        category_name = request.POST.get('name')
        description = request.POST.get('description')
        category_image = request.FILES.get('Image')
        status = request.POST.get('status')
        obj = CategoryDb(category_image=category_image,description=description,category_name=category_name,status=status)
        obj.save()
        messages.success(request, "Category added successfully!")
        return redirect(Categories_Add)

def Category_View(request):
    data = CategoryDb.objects.all()
    return render(request,'Categories_View.html',{'data':data})

def Category_Edit(request,t_id):
    data = CategoryDb.objects.get(id=t_id)
    return  render(request,'Categories_Edit.html',{'data':data})
def Category_update(request,c_id):
    category_name = request.POST.get('name')
    description = request.POST.get('description')
    status = request.POST.get('status')

    try:
        img = request.FILES['Image']
        obj = FileSystemStorage()
        file =obj.save(img.name,img)
    except MultiValueDictKeyError:
        file = CategoryDb.objects.get(id=c_id).category_image
    CategoryDb.objects.filter(id=c_id).update(category_name=category_name,description=description,status=status,category_image=file)
    messages.success(request, "Category Updates successfully!")
    return redirect(Category_View)


def Category_delete(request,c_id):
    data = CategoryDb.objects.filter(id =c_id)
    data.delete()
    messages.success(request, "Category Deleted successfully!")
    return redirect(Category_View)


def Food_Add(request):
    data=CategoryDb.objects.all()
    return render(request,'Food_Add.html',{'data':data})

def Food_Save(request):
    if request.method == "POST":
        food_name = request.POST.get('fname')
        category_name = request.POST.get('cname')
        description = request.POST.get('description')
        price = request.POST.get('Price')
        availability = request.POST.get('status')
        food_image = request.FILES.get('Image')
        obj = FoodDb(food_name=food_name,category_name=category_name,description=description,price=price,avialable=availability,food_image=food_image)
        obj.save()
        messages.success(request, "Food added successfully!")
    return redirect(Food_Add)

def food_view(request):
    data = FoodDb.objects.all()
    return render(request,'Food_View.html',{'data':data})


def Food_delete(request,c_id):
    data = FoodDb.objects.filter(id =c_id)
    data.delete()
    data1=FoodDb.objects.all()
    messages.success(request, "Food item Deleted successfully!")
    return redirect(food_view,{'data1':data1})

def Food_Edit(request,c_id):
    data=FoodDb.objects.all()
    return render(request,'Food_Edit.html',{'data':data})

def Food_update(request,c_id):
    category_name = request.POST.get('cname')
    food_name=request.POST.get('fname')
    description = request.POST.get('description')
    price = request.POST.get('prie')
    avialable=request.POST.get('avialable')

    try:
        img = request.FILES['Image']
        obj = FileSystemStorage()
        file =obj.save(img.name,img)
    except MultiValueDictKeyError:
        file = FoodDb.objects.get(id=c_id).food_image
        FoodDb.objects.filter(id=c_id).update(food_name=food_name,category_name=category_name,description=description,
                                              price=price,avialable=avialable,food_image=file)
    messages.success(request, "Food Item Updates successfully!")
    return redirect(food_view)


def Staff_add(request):
    return render(request,'Staff_Add.html')

def Staff_Save(request):
    if request.method == "POST":
        name = request.POST.get('sname')
        age = request.POST.get('Age')
        role = request.POST.get('Role')
        salary = request.POST.get('Salary')
        email = request.POST.get('email')
        phone = request.POST.get('Mobile')
        adress = request.POST.get('Address')
        profile = request.FILES.get('Image')

        obj=StaffDb(staff_name=name,staff_age=age,staff_salary=salary,staff_email=email,staff_phone=phone,role=role,
                    profile_image=profile,staff_Address=adress)
        obj.save()
    return redirect(Staff_add)
def Staff_View(request):
    data = StaffDb.objects.all()
    return render(request,'Staff_View.html',{'data':data})

def Staff_Delete(request,c_id):
    data = StaffDb.objects.filter(id =c_id)
    data.delete()
    messages.success(request, "Staff Deleted successfully!")
    return redirect(Staff_View)


def Staff_Edit(request,t_id):
    data = StaffDb.objects.get(id=t_id)
    return render(request,'Staff_Edit.html',{'data':data})


def Staff_Update(request,s_id):
    name = request.POST.get('sname')
    age = request.POST.get('Age')
    role = request.POST.get('Role')
    salary = request.POST.get('Salary')
    email = request.POST.get('email')
    phone = request.POST.get('Mobile')
    adress = request.POST.get('Address')
    profile = request.FILES.get('Image')

    try:
        img = request.FILES['Image']
        obj = FileSystemStorage()
        file =obj.save(img.name,img)
    except MultiValueDictKeyError:
        file = StaffDb.objects.get(id=s_id).profile_image
    StaffDb.objects.filter(id=s_id).update(staff_name=name,staff_age=age,staff_salary=salary,staff_email=email,staff_phone=phone,role=role,
                    profile_image=file,staff_Address=adress)
    messages.success(request, "Staff Updated successfully!")
    return redirect(Staff_View)

def view_orders(request):
    orders = OrderModel.objects.all().order_by('-id')

    context = {
        "orders": orders
    }

    return render(request, "Order_view.html", context)


def Table_Add(request):
    return render(request,'Table_Add.html')


def table_save(request):
    if request.method == "POST":
        t_num = request.POST.get('tnum')
        t_capacity = request.POST.get('capacity')
        t_active=request.POST.get('active')

        obj=TableDB(Table_no=t_num,Capacity=t_capacity,active=t_active)
        obj.save()
    return redirect(table_add)

def table_view(request):
    data =TableDB.objects.all()
    return render(request,'Table_view.html',{'data':data})

def table_Edit(request,t_id):
    data = TableDB.objects.get(id=t_id)
    return render(request,'Table_Edit.html',{'data':data})
def table_update(request,t_id):
    t_num = request.POST.get('tnum')
    t_capacity = request.POST.get('capacity')
    t_active = request.POST.get('active')
    TableDB.objects.filter(id=t_id).update(Table_no=t_num,Capacity=t_capacity,active=t_active)
    messages.success(request, "Table Updated successfully!")
    return redirect(table_view)

def Table_Delete(request,t_id):
    data = StaffDb.objects.filter(id =t_id)
    data.delete()
    messages.success(request, "Staff Deleted successfully!")
    return redirect(table_view)

def view_reservation(request):

    bookings = BookingDB.objects.all().order_by("-booking_date", "-booking_time")

    return render(request, "Reservations_view.html", {"bookings": bookings})


def edit_booking(request, id):

    booking = get_object_or_404(BookingDB, id=id)
    tables = TableDB.objects.filter(active="Yes")

    if request.method == "POST":

        booking.customer_name = request.POST.get("customer_name")
        booking.phone = request.POST.get("phone")
        booking.email = request.POST.get("email")
        booking.booking_date = request.POST.get("booking_date")
        booking.booking_time = request.POST.get("booking_time")
        booking.guests = request.POST.get("guests")
        booking.status = request.POST.get("status")

        table_id = request.POST.get("table")
        booking.table = get_object_or_404(TableDB, id=table_id)

        booking.save()

        return redirect("view_reservation")

    return render(request, "Reservation_Edit.html", {
        "booking": booking,
        "tables": tables
    })


def delete_booking(request, id):

    booking = get_object_or_404(BookingDB, id=id)
    booking.delete()
    return redirect("view_reservation")


def view_orders(request):
    orders = OrderModel.objects.all().order_by("-id")
    context = {
        "orders": orders,

    }

    return render(request, "Order_view.html", context)

def order_details(request, order_id):
    order = get_object_or_404(OrderModel, id=order_id)

    items = OrderItem.objects.filter(Order=order)

    context = {
        "order": order,
        "items": items,
    }

    return render(request, "Order_Details.html", context)

def cancel_order(request, order_id):
    order = OrderModel.objects.get(id=order_id)

    order.Order_Status = "Cancelled"
    order.save()

    messages.success(request, "Order cancelled successfully.")
    return redirect("view_orders")




