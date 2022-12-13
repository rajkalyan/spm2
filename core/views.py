from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cart, Products, User,Rolereq
from .forms import ProductForm, RegForm,Chgepwd,Pfupd,Rltype,Rlupd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date

# Create your views here.
def home(request):
    return render(request,'html/index.html')

def usrreg(request):
    if request.method=="POST":
        d = RegForm(request.POST,request.FILES)
        if d.is_valid():
            d.save()
            return redirect('/login')
    d = RegForm()
    return render(request,'html/register.html',{'t':d})

@login_required
def changepwd(request):
    if request.method == "POST":
        k = Chgepwd(user=request.user,data=request.POST)
        if k.is_valid():
            k.save()
            return redirect('/login')
    k = Chgepwd(user=request)
    return render(request,'html/changePassword.html',{'t':k})

@login_required
def pfle(request):
    x = User.objects.get(id=request.user.id)
    return render(request,'html/profile.html',{'d':x})

@login_required
def pfupd(request):
    d=User.objects.get(id=request.user.id)
    if request.method=="POST":
        pf=Pfupd(request.POST,request.FILES,instance=d)
        if pf.is_valid():
            pf.save()
            return redirect('/profile')
    pf=Pfupd(instance=d)
    return render(request,'html/profileUpdate.html',{'u':pf})

@login_required
def rolereq(request):
    p = Rolereq.objects.filter(ud_id=request.user.id).count()
    if request.method == "POST":
        k =Rltype(request.POST,request.FILES)
        if k.is_valid:
            y = k.save(commit = False)
            y.ud_id = request.user.id
            y.uname = request.user.username
            y.is_checked = 0
            y.save()
            return redirect('/')
    k = Rltype()
    return render(request,'html/rolerequest.html',{'d':k,'c':p})

@login_required
def gveperm(request):
    u = User.objects.all()
    r = Rolereq.objects.all()
    d = {}
    for n in u:
        for m in r:
            if n.is_superuser == 1 or n.id != m.ud_id:
                continue
            else:
                d[m.id] = n.username,m.rltype,n.role,n.id,m.id
    return render(request,'html/gvper.html',{'h':d.values()})

@login_required
def gvupd(request,t):
    y=Rolereq.objects.get(ud_id=t)
    d=User.objects.get(id=t)
    if request.method == "POST":
        n = Rlupd(request.POST,instance=d)
        if n.is_valid():
            n.save()
            #d.role = s.rltype
            y.is_checked = 1
            y.save()
            return redirect('/gvper')
    n = Rlupd(instance=d)
    return render(request,'html/gvepermissions.html',{'c':n})

@login_required
def reqdel(request,t):
    r = Rolereq.objects.get(id=t)
    u = User.objects.get(id=r.ud_id)
    if request.method == "POST":
        u.role=1
        r.delete()
        u.save()
        messages.success(request,"Request from {} Deleted Successfully".format(u.username))
        return redirect('/gvper')
    return render(request,'html/reqdel.html',{'a':u})

@login_required
def addproduct(request):
    d = Products.objects.filter(wid_id=request.user.id)
    if request.method=="POST":
        r=ProductForm(request.POST,request.FILES)
        if r.is_valid:
            c = r.save(commit=False)
            c.wid_id = request.user.id
            c.save()
            messages.success(request,"Product Added Successfully")
            return redirect('/addproduct')
    r = ProductForm()
    return render(request,'html/addProduct.html',{'a':r,'x':d})

@login_required
def updtproduct(request,m):
    d = Products.objects.get(id=m)
    if request.method == "POST":
        r = ProductForm(request.POST,request.FILES,instance=d)
        if r.is_valid():
            r.save()
            messages.info(request,"Product Updated Successfully")
            return redirect('/addproduct')
    r = ProductForm(instance=d)
    return render(request,'html/updtProduct.html',{'c':r})

@login_required
def delproduct(request,m):
    d = Products.objects.get(id=m)
    if request.method=="POST":
        d.delete()
        messages.success(request,"{} Product Deleted Successfully".format(d.pno))
        return redirect('/addproduct')
    return render(request,'html/delProduct.html',{'x':d})

@login_required
def viewproduct(request,m):
    d = Products.objects.get(id=m)
    return render(request,'html/viewProduct.html',{'x':d})

def allproducts(request):
    d = Products.objects.all()
    if request.method=="POST":
        p=request.POST['pno']
        q=request.POST['pname']
        r=request.POST['pcost']
        t=request.POST['quantity']
        s=int(t)*float(r)
        v=request.POST['id']
        k=Cart(pid=p,pname=q,pcost=s,uid_id=request.user.id,quant=t,proid_id=v)
        k.save()
        return redirect('/products')
    return render(request,'html/allProducts.html',{'x':d})

@login_required
def cart(request):
    d=Cart.objects.filter(uid_id=request.user.id,is_bought=0)
    return render(request,'html/cart.html',{'x':d})

@login_required
def deletecart(request,m):
    d = Cart.objects.get(id=m)
    if request.method=="POST":
        d.delete()
        messages.success(request,"{} Product Deleted from cart Successfully".format(d.pname))
        return redirect('/cart')
    return render(request,'html/delCart.html',{'x':d})

def contact(request):
    return render(request,'html/contactus.html')

def about(request):
    return render(request,'html/aboutus.html')

def TermsandConditions(request):
    return render(request,'html/TermsandConditions.html')

@login_required
def buynow(request,m):
    d=Cart.objects.filter(uid_id=request.user.id,is_bought=0)
    for i in d:
        i.is_bought=1
        i.save()
    return redirect('/')

@login_required
def history(request,m):
    d=Cart.objects.filter(uid_id=request.user.id, is_bought=1)
    return render(request,'html/history.html',{'x':d})
