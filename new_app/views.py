from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import Login_Form, CustomerRegisterForm, StockForm
from new_app.models import CustomerRegister, Stock


# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url = 'login_page')
def indexx(request):
    return render(request,"indexx.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("adminbase")
            if user.is_customer:
                return redirect("customerbase")
        else:
            messages.info(request,"Invalid credentials")
    return render(request,"login.html")


################ADMIN#################

@login_required(login_url = 'login_page')
def adminbase(requset):
    return render(requset,"admin/admin base.html")

@login_required(login_url = 'login_page')
def add_stock(request):
    form = StockForm()
    if request.method =='POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers_data")
    return render(request,'admin/add_stock.html',{'form':form})

@login_required(login_url = 'login_page')
def view_stock(request):
    data = Stock.objects.all()
    return render(request,'admin/view_stock.html',{'data':data})



@login_required(login_url = 'login_page')
def customers_data(request):
    data = CustomerRegister.objects.all()
    print(data)
    return render(request,"admin/customers_data.html",{'data':data})


@login_required(login_url = 'login_page')
def update(request, id):

        a = Stock.objects.get(id=id)
        form = StockForm(instance=a)
        if request.method == 'POST':
            form = StockForm(request.POST, instance=a)
            if form.is_valid():
                form.save()
                return redirect("view_stock")

        return render(request, "admin/update.html", {'form': form})

@login_required(login_url = 'login_page')
def delete_stock(request,id):
    wm = Stock.objects.get(id=id)
    wm.delete()
    return redirect("view_stock")




#################CUSTOMER##################

@login_required(login_url = 'login_page')
def customerbase(requset):
    return render(requset,"customer/customer base.html")

def customer_register(request):
    form1 = Login_Form()
    form2 = CustomerRegisterForm()
    if request.method == "POST":
        form1 = Login_Form(request.POST)
        form2 = CustomerRegisterForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request,"customer/customer_register.html",{'form1':form1,'form2':form2})


@login_required(login_url = 'login_page')
def view_customers_data(request):
    data = Stock.objects.filter(id=2).order_by('-id')[:1]
    return render(request,'customer/view_customers_data.html',{'data':data})



def logout_view(request):
    logout(request)
    return redirect("login_page")