from django.shortcuts import render,redirect
from AdminApp.models import *
from WebApp.models import ContactDb, AccountDb, CartDb


# Create your views here.
def home(request):
    categories=CategoryDb.objects.all()
    latest_products=ProductDb.objects.order_by('-id')[:8]
    return render(request,"Home.html",{'categories':categories,
                                       "latest_products":latest_products})
def all_products(request):
    categories=CategoryDb.objects.all()
    products=ProductDb.objects.all()
    latest_products=ProductDb.objects.order_by('-id')[:3]
    return render(request,"All_Products.html",{'categories':categories ,
                                               'products':products,
                                               "latest_products":latest_products })
def filtered_product(request,cat_name):
    product_filtered=ProductDb.objects.filter(Product_Category=cat_name)
    return render(request,'Filtered_Product.html',{'product_filtered':product_filtered})


def single_item(request,product_id):
    single_product=ProductDb.objects.get(id=product_id)
    return render(request,"Single_item.html",{'single_product':single_product})

def contact(request):
    details=ContactDb.objects.all()
    return render(request,"Contact.html",{'details':details})
def save_contact(request):
    if request.method=='POST':
        con_name= request.POST.get('name')
        con_email= request.POST.get('email')
        con_message= request.POST.get('message')
        obj=ContactDb(Name=con_name,Email=con_email,Message=con_message)
        obj.save()
        return redirect(contact)
def sign_in(request):
    return render(request,'Sign_in.html')
def sign_up(request):
    return render(request,'Sign_Up.html')

def save_account(request):
    if request.method=='POST':
        acc_username=request.POST.get('username')
        acc_email=request.POST.get('email')
        acc_password=request.POST.get('password')
        con_password=request.POST.get('con_password')
        obj=AccountDb(Username=acc_username,Email=acc_email,Password=acc_password,Confrom_Password=con_password)
        if AccountDb.objects.filter (Username=acc_username,Password=acc_password).exists():
            print("Username already exist...")
            return redirect(sign_up)
        elif AccountDb.objects.filter(Email=acc_email).exists():
            print("Email already exist")
            return redirect(sign_up)
        else:
            obj.save()
            return redirect(sign_in)

def user_loging(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        if AccountDb.objects.filter(Username=uname,Password=pswd).exists():
            request.session['Username']=uname
            request.session['Password']=pswd
            return redirect(home)
        else:
            return redirect(sign_up)
    else:
        return redirect(sign_up)
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home)

def shoping_cart(request):
    cart=CartDb.objects.filter(Username=request.session['Username'])
    sub_total=0
    delivery=0
    grand_total=0
    user_date=CartDb.objects.filter(Username=request.session['Username'])
    for i in user_date:
        sub_total += i.Total_Price
        if sub_total > 1000:
            delivery = 0
        elif sub_total > 500:
            delivery = 50
        else:
            delivery=100
        grand_total=sub_total + delivery

    return render(request,'Shoping_Cart.html',{'cart':cart,
                                               'sub_total':sub_total,
                                              'delivery':delivery,
                                              'grand_total':grand_total })
def service(request):
    return render(request,'Service.html')
def save_cart(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        proname=request.POST.get('productname')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        tprice=request.POST.get('totalprice')
        pro=ProductDb.objects.filter(Product_Name=proname).first()
        img = pro.Product_Image if pro else None
        obj=CartDb(Username=uname,ProductName=proname,Quantity=quantity,Price=price,Total_Price=tprice,Product_Image=img)
        obj.save()
        return redirect(home)


