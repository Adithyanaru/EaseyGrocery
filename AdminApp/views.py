from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDict, MultiValueDictKeyError
from pyexpat.errors import messages
from django.contrib import messages

from WebApp.models import ContactDb

from AdminApp.models import CategoryDb,ProductDb


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')
def add_products(request):
    category = CategoryDb.objects.all()
    return render(request,'Add_Products.html', {'Category': category})
def view_products(request):
    product=ProductDb.objects.all()
    return render(request,'View_Products.html',{"Product":product})


#---------Catagory-----------

def add_catagory(request):
    return render(request,'Add_Catagory.html')
def view_catagory(request):
    category=CategoryDb.objects.all()
    return render(request,'View_Catagory.html', {"Category":category})



def login(request):
    return render(request,'Login.html')

def admin_login(request):
    uname=request.POST.get('username')
    pswd=request.POST.get('password')
    if User.objects.filter(username__contains=uname).exists():
        user=authenticate(username=uname,password=pswd)
        if user is not None:
            # login(request,user)
            request.session['username']=uname
            request.session['password']=pswd

            return redirect(dashboard)
        else:
            return redirect(login)
    else:
        return redirect(login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login)

#Save category, save in database
def save_category(request):
    if request.method == "POST":
        cat_name = request.POST.get("name")
        cat_desc = request.POST.get("Description")
        cat_img = request.FILES["img"]
        obj=CategoryDb(CategoryName=cat_name,Description=cat_desc,CategoryImage=cat_img)
        obj.save()
        messages.success(request,'Category Added')
        return redirect(add_catagory)

def delete_category(request,cat_id):
    cat=CategoryDb.objects.filter(id=cat_id)
    cat.delete()
    return redirect(view_catagory)
# def edit_category(request, cat_id):
#     category=CategoryDb.objects.get(id=cat_id)
#     return render(request,"Edit_Category.html",{"cat":category})
def edit_category(request, cat_id):
    category = get_object_or_404(CategoryDb, id=cat_id)
    return render(request, "Edit_Category.html",  {"category": category})

def update_category(request,catg_id):
    if request.method=="POST":
        cat_name=request.POST.get("name")
        cat_desc=request.POST.get("Description")
        try:
            cat_img= request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(cat_img.name,cat_img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=catg_id).CategoryImage
        CategoryDb.objects.filter(id=catg_id).update(CategoryName=cat_name,Description=cat_desc,CategoryImage=file)
        return redirect(view_catagory)

#---------product----
def save_product(request):
    if request.method == "POST":
        pro_name=request.POST.get("name")
        pro_cat=request.POST.get("category")
        pro_prize=request.POST.get("prize")
        pro_desc=request.POST.get("desc")
        pro_image=request.FILES["img"]
        obj=ProductDb(Product_Name=pro_name,Product_Category=pro_cat,Prize=pro_prize,Description=pro_desc,
                      Product_Image=pro_image)
        messages.success(request, 'Product Added')
        obj.save()
        return redirect(add_products)
def delete_product(request,p_id):
    pro=ProductDb.objects.filter(id=p_id)
    pro.delete()
    return redirect(view_products)
def edit_product(request,pro_id):
    products=ProductDb.objects.get(id=pro_id)
    return render(request,"Edit_Product.html",{'pro':products})

def update_product(request,pro_id):
    if request.method=="POST":
        pro_name=request.POST.get("name")
        pro_cat=request.POST.get("category")
        pro_prize=request.POST.get("prize")
        pro_desc=request.POST.get("desc")
        try:
            pro_img=request.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(pro_img.name,pro_img)
        except MultiValueDictKeyError:
            file=ProductDb.objects.filter(id=pro_id).Product_Image
        ProductDb.objects.filter(id=pro_id).update(Product_Name=pro_name,Product_Category=pro_cat,
                                                    Prize=pro_prize,Description=pro_desc,Product_Image=file)
        return redirect(view_products)

def contact_details(request):
    con_details=ContactDb.objects.all()
    return render(request,'Contact_Details.html',{'con_details':con_details})
