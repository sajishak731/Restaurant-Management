from django.shortcuts import render,redirect
from AdminApp.models import CategoryDb,FoodDb,StaffDb
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage


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
    return render(request,'Food_Add.html')

def Food_Save(request):
    if request.method == "POST":
        food_name = request.POST.get('fname')
        category_name = request.POST.get('cname')
        description = request.POST.get('description')
        price = request.POST.get('Price')
        availability = request.POST.get('Availability')
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
    messages.success(request, "Food item Deleted successfully!")
    return redirect(food_view)

def Food_Edit(request):
    return render(request,'Food_Edit.html')

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









