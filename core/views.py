from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Product,Addres,Cart,OrderPlaced,Contact,ProductReview
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    product_Brand = Product.objects.all().order_by('-id')[:5]
    
    total_cart = 0
    
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    return render(request,"index.html",{"total_cart":total_cart,"brands":product_Brand})

def alltires(request):
    total_cart = 0

    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    products = Product.objects.all()
    proDic = {"products":products,"total_cart":total_cart}
    return render(request,"alltires.html",proDic)

@login_required(login_url='/login')
def productDetails(request,id):
    total_cart = 0

    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    product= Product.objects.filter(id=id).first()
    is_item_present = False
    comments = ProductReview.objects.filter(post=product).order_by('-Date')
    is_item_present = Cart.objects.filter(
        Q(product=product.id) & Q(user=request.user))
    proDic = {"products":product,"is_item_present": is_item_present,"total_cart":total_cart,"comments":comments}
    return render(request,"productDetails.html",proDic,)

def learn(request):
    total_cart = 0

    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    return render(request,"learn.html",{"total_cart":total_cart})


def search(request):
    total_cart = 0
    product_Brand = Product.objects.all().order_by('-id')[:5]
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    query = request.GET['search']
    search_filter = Product.objects.filter(Q(title__icontains=query) | Q(brand__icontains=query) )
    search_dic = {"search": search_filter, "query": query,"total_cart":total_cart,"brands":product_Brand}
    return render(request, "search.html", search_dic)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        userLogin = authenticate(username=username, password=password)
        if userLogin is not None:
            login(request, userLogin)
            messages.success(request, "Welcome " + username)
            return redirect('/')
        else:
            messages.warning(request, "Please check your username or password")
            return redirect('login')
    return render(request, "login.html")


def registerUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).first():
            messages.warning(
                request, "This username already exists")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            messages.success(
                request, " Your account has been created successfully ")
            return redirect('login')

    return render(request, "register.html")


def logoutUser(request):
    logout(request)
    messages.success(request,"You have been loggedOut")
    return redirect("login")
    return HttpResponse("You have been loggedOut")

@login_required(login_url='/login')
def profile(request):
     total_cart = 0

     if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
     if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        user = request.user
        costumer = Addres(user=user,name=name,address=address,address2=address2,city=city,zipcode=zip,state=state)
        costumer.save()
        messages.success(request, "Address is been added successfully")
   
     return render(request,"profile.html",{"total_cart":total_cart})

@login_required(login_url='/login')
def address(request): 
        total_cart = 0

        
        if request.user.is_authenticated:
            total_cart = len(Cart.objects.filter(user=request.user))
            address = Addres.objects.filter(user=request.user)
            addres_di= {'address':address,"total_cart":total_cart}

        return render(request, 'address.html',addres_di)

def map(request):
    total_cart = 0

    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    return render(request,"map.html",{"total_cart":total_cart})
    
@login_required(login_url='/login')
def cart(request):
    user = request.user
    product_id = request.GET.get("product_id")
    product = Product.objects.get(id=product_id)
    Mycart = Cart(user=user,product=product)
    Mycart.save()

    return redirect("/showcart")

@login_required(login_url='/login')
def showcart(request):

    total_cart = 0

    if request.user.is_authenticated:
        user = request.user
        allcarts = Cart.objects.filter(user=user).order_by('-date')
        total_cart = len(Cart.objects.filter(user=request.user))

        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0

        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if(cart_product):
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount

            cartDic = {"allcart": allcarts, "amount": amount,
                       "totalamount": amount + shipping_amount, "total_cart": total_cart}
        else:
            return render(request, 'emptyCart.html')

    return render(request, 'showcart.html', cartDic)




# def showcart(request):

#     total_cart = 0

#     if request.user.is_authenticated:
#         user = request.user
#         allcarts = Cart.objects.filter(user=user).order_by('-date')
#         total_cart = len(Cart.objects.filter(user=request.user))

#         amount = 0.0
#         shipping_amount = 50.0
#         total_amount = 0.0

#         cart_product = [p for p in Cart.objects.all() if p.user == user]

#         if(cart_product):
#             for p in cart_product:
#                 tempamount = (p.quantity * p.product.price)
#                 amount += tempamount

#             cartDic = {"allcart": allcarts, "amount": amount,
#                        "totalamount": amount + shipping_amount, "total_cart": total_cart}
#         else:
#             return render(request, 'emptyCart.html')

#     return render(request, 'showcart.html', cartDic)


@login_required(login_url='/login')
def pluscart(request):
    if request.method == "GET":
        pro_id = request.GET['pro_id']

        c = Cart.objects.get(Q(product=pro_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0

        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]

        if(cart_product):
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount

            data = {
                "quantity": c.quantity,
                "amount": amount,
                "totalamount": amount + shipping_amount
            }
            return JsonResponse(data)

@login_required(login_url='/login')
def minuscart(request):
    if request.method == "GET":
        pro_id = request.GET['pro_id']

        c = Cart.objects.get(Q(product=pro_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0

        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]

        if(cart_product):
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount

            data = {
                "quantity": c.quantity,
                "amount": amount,
                "totalamount": amount + shipping_amount

            }
            return JsonResponse(data)

@login_required(login_url='/login')
def removecart(request):
    if request.method == "GET":
        pro_id = request.GET['pro_id']

        c = Cart.objects.get(Q(product=pro_id) & Q(user=request.user))

        c.delete()
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0

        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]

        if(cart_product):
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount
                totalamount = amount + shipping_amount

            data = {

                "amount": amount,
                "totalamount": totalamount
            }
            return JsonResponse(data)
@login_required(login_url='/login')
def checkout(request):
    adresss = len(Addres.objects.filter(user=request.user))
    if(adresss):
            allcarts = Cart.objects.filter(user=request.user)
            alladress = Addres.objects.filter(user=request.user)

            amount = 0.0
            shipping_amount = 50.0
            total_amount = 0.0

            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            total_cart = 0
            if request.user.is_authenticated:
                total_cart = len(Cart.objects.filter(user=request.user))
            if(cart_product):
                for p in cart_product:
                    tempamount = (p.quantity * p.product.price)
                    amount += tempamount
                totalamount = amount + shipping_amount

            shopingDetailDic = {"carts": allcarts, "address": alladress,
                                "amount": totalamount, "total_cart": total_cart}
            return render(request, 'checkout.html', shopingDetailDic,)
    else:
        return render(request,"noAdress.html")

   

@login_required(login_url='/login')
def paymentdone(request):
    user = request.user
    customerId = request.GET.get("custadd")
    costumer = Addres.objects.get(id=customerId)
    carts = Cart.objects.filter(user=user)

    for c in carts:
        OrderPlaced(user=user, costumer=costumer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()

    return redirect("/orders")
@login_required(login_url='/login')
def orders(request):
    total_cart = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    allOrders = OrderPlaced.objects.filter(
        user=request.user).order_by('-ordered_date')

    return render(request, 'orders.html', {"orders": allOrders, "total_cart": total_cart})


def contact(request):
    if request.method == 'POST':
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contact = Contact(fullname=fullname, email=email,
                          phone=phone, message=message)
        contact.save()
        messages.success(request, "Thanks for contacting us " + fullname)

    return render(request, "contact.html")


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postid = request.POST.get('postSno')
        post = Product.objects.get(id=postid)
        comment = ProductReview(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your review has been posted successfully")

        return redirect(f"productDetails/{postid}")
    else:
      return HttpResponse("404 Error")


def filters(request,filter):
    product_Brand = Product.objects.all().order_by('-id')[:5]
    filter = Product.objects.filter(brand=filter)
    fDic = {"filterBrand":filter,"brands": product_Brand}
    return render(request,"filters.html",fDic)


def TireSize(request):
    total_cart = 0
    product_Brand = Product.objects.all().order_by('-id')[:5]
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    query = request.GET['tireSize']
    search_filter = Product.objects.filter(tire_size=query)
    search_dic = {"filterBrand": search_filter, "query": query,"total_cart":total_cart,"brands":product_Brand}
    return render(request, "tireSizeFilter.html", search_dic)


def Vehicle(request):
    total_cart = 0
    product_Brand = Product.objects.all().order_by('-id')[:5]
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
    query = request.GET['vehicle']
    search_filter = Product.objects.filter(vehicle=query)
    search_dic = {"filterBrand": search_filter, "query": query,"total_cart":total_cart,"brands":product_Brand}
    return render(request, "VehicleFilter.html", search_dic)

