from django.shortcuts import render
from .models import mentrouser
from .models import womentrouser
from .models import womenshirt
from .models import menshirt
from .models import equipment
from .models import newarrival
from .models import contactForm
from .models import order
# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.core import serializers
import json
def home(request):
    wt = womentrouser.objects.order_by('-post_id').all()
    mt = mentrouser.objects.order_by('-post_id').all()
    ws = womenshirt.objects.order_by('-post_id').all()
    ms = menshirt.objects.order_by('-post_id').all()
    na = newarrival.objects.order_by('-post_id').all()
    eq = equipment.objects.order_by('-post_id').all()

    return render(request, "mart/home.html", {'na': na[:8], 'wt': wt[:8], 'mt': mt[:8], 'ws': ws[:8], 'ms': ms[:8], 'eq': eq[:8]})

def naproduct_detail(request, id):
    na = newarrival.objects.filter(post_id=id)[0]
    return render(request, "mart/naview-product.html", {'t': na})

def wtproduct_detail(request, id):
    wt = womentrouser.objects.filter(post_id=id)[0]
    return render(request, "mart/naview-product.html", {'t': wt})

def wsproduct_detail(request, id):
    ws = womenshirt.objects.filter(post_id=id)[0]
    return render(request, "mart/naview-product.html", {'t': ws})

def mtproduct_detail(request, id):
    mt = mentrouser.objects.filter(post_id=id)[0]
    return render(request, "mart/naview-product.html", {'t': mt})

def msproduct_detail(request, id):
    ms = menshirt.objects.filter(post_id=id)[0]
    return render(request, "mart/naview-product.html", {'t': ms})

def eqproduct_detail(request, id):
    eq = equipment.objects.filter(post_id=id)[0]
    return render(request, "mart/naview-product.html", {'t': eq})


def newarrivals(request):
    na = newarrival.objects.order_by('-post_id').all()
    category = "New Arrivals"
    return render(request, "mart/na-products.html", {'t': na , 'cat': category})


def womentrousers(request):
    wt = womentrouser.objects.order_by('-post_id').all()
    category = "Women Trousers/Leggings/Tights/Jeans"
    return render(request, "mart/wt-products.html", {'t': wt , 'cat': category})


def mentrousers(request):
    mt = mentrouser.objects.order_by('-post_id').all()
    category = "Men Trousers/Jeans"
    return render(request, "mart/mt-products.html", {'t': mt, 'cat': category})

def menshirts(request):
    ms = menshirt.objects.order_by('-post_id').all()
    category = 'Men Shirts/T-Shirts'
    # link = "msdetail/{{item.post_id}}"
    return render(request, "mart/ms-products.html", {'t': ms, 'cat':category})



def womenshirts(request):
    ws = womenshirt.objects.order_by('-post_id').all()
    category = 'Women Shirts/T-Shirts'
    return render(request, "mart/ws-products.html", {'t': ws, "cat":category})


def machine(request):
    eq = equipment.objects.order_by('-post_id').all()
    category = 'Equipments'
    return render(request, "mart/eq-products.html", {'t': eq , 'cat':category})


def contact(request):
    if request.method=="POST":
        name = request.POST.get("fname", 'e')
        email = request.POST.get("email")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        message =  request.POST.get("message")

        # if name==False:
        #     print(name)
        #     fill_all_entries = "Please fill all Fields."
        #     return render(request, "mart/thankyou.html", {'message': fill_all_entries})

        thankyou_message = "Thank You For Contacting"
        print(name,email,city,phone,message)
        contact = contactForm(name=name, email=email, city=city, phone=phone, message=message)
        contact.save()
        return render(request, "mart/thankyou.html", {'message': thankyou_message})
    message = "Contact"
    return render(request,"mart/contact.html", {'message': message})



#{'object[0][name]': ['9'], 'object[0][id]': ['9'], 'object[0][price]': ['3'], 'object[0][qty]': ['1'], 'object[0][category]': ['ttt'], 'csrfmiddlewaretoken': ['8HF6hyuHhXx8U7xVoNBkz3Z4LYmnR3miPuayWAu2hD9JsNIsbvnjbVdCmNlK05p2']}



@csrf_protect
def checkoutnow(request):
    my_dict = {}
    name_dict = {}
    final_dict = {}
    record=0
    total_price = 0

    if request.method == 'POST':

        print(type(request.POST))
        m = request.POST

        print("length",len(m))
        for k,v in m.items():
            print(k,"and ", v)
            my_dict.update({k: v})
        key = my_dict.pop("csrfmiddlewaretoken")
        #print(my_dict)
        print(key)


        for p in range(int(len(my_dict)/5)):
            name = m[f'object[{p}][name]']
            qty =  m[f'object[{p}][qty]']
            name_dict.update({name: qty})

        #print("zz",name_dict)

        for n, q in name_dict.items():

            print(n , q)



            if newarrival.objects.filter(product_name__contains=n):
                db = newarrival.objects.filter(product_name__contains=n)
                print("price",db[0].price * int(q))
                price = db[0].price * int(q)
                print("na", price)
            elif womentrouser.objects.filter(product_name__contains=n):
                db = womentrouser.objects.filter(product_name__contains=n)
                print("price", db[0].price)
                price = db[0].price * int(q)
                print("wt",price)
            elif womenshirt.objects.filter(product_name__contains=n):
                db = womenshirt.objects.filter(product_name__contains=n)
                print("price", db[0].price)
                price = db[0].price * int(q)
                print("ws",price)
            elif mentrouser.objects.filter(product_name__contains=n):
                db = mentrouser.objects.filter(product_name__contains=n)
                print("price", db[0].price)
                price = db[0].price * int(q)
                print("mt",price)
            elif menshirt.objects.filter(product_name__contains=n):
                db = menshirt.objects.filter(product_name__contains=n)
                print("price", db[0].price)
                price = db[0].price * int(q)
                print("ms",price)
            elif equipment.objects.filter(product_name__contains=n):
                db = equipment.objects.filter(product_name__contains=n)
                print("price", db[0].price)
                price = db[0].price * int(q)
                print("eq",price)
            else:
                print("didnt match")

            d = {record: [n, q, price]}
            record = record + 1
            final_dict.update(d)
    print(final_dict)
   # print(final_dict[1][2])
    print(len(final_dict))
    for j in range(int(len(final_dict))):
        print("this is j",j)
        total_price += final_dict[j][2]
    print(total_price)
    return JsonResponse({"ok": ""}, status=200)
    #return render(request, "mart/checkout.html", {"total": total_price, "final_bill": final_dict, "csrfmiddlewaretoken": key})
   # return render(request, "mart/checkout.html")

def checkout(request):

    return render(request, "mart/checkout.html")
def searchin(request):
    query = request.GET.get('search')
    wt = womentrouser.objects.all()
    ws = womenshirt.objects.all()
    ms = menshirt.objects.all()
    mt = mentrouser.objects.all()
    na = newarrival.objects.all()
    eq = equipment.objects.all()
    searched_products = []
    print("marting ")
    for item in eq:
        word = item.product_name.lower().split()

        if query in word:
            searched_products.append(item)
            print(item.product_name, "this is filte...!!!!!!!!!!!")
    for t in searched_products:
        print(t, "from the list")

    for item in wt:
        word = item.product_name.lower().split()

        if query in word:
            searched_products.append(item)
            print(item.product_name, "this is filte...!!!!!!!!!!!")
    for t in searched_products:
        print(t, "from the list")


    for item in ws:
        word = item.product_name.lower().split()

        if query in word:
            searched_products.append(item)
            print(item.product_name, "this is filte...!!!!!!!!!!!")
    for t in searched_products:
        print(t, "from the list")



    for item in mt:
        word = item.product_name.lower().split()

        if query in word:
            searched_products.append(item)
            print(item.product_name, "this is filte...!!!!!!!!!!!")
    for t in searched_products:
        print(t, "from the list")


    for item in ms:
        word = item.product_name.lower().split()

        if query in word:
            searched_products.append(item)
            print(item.product_name, "this is filte...!!!!!!!!!!!")
    for t in searched_products:
        print(t, "from the list")


    for item in na:
        word = item.product_name.lower().split()

        if query in word:
            searched_products.append(item)
            print(item.product_name, "this is filte...!!!!!!!!!!!")
    for t in searched_products:
        print(t, "from the list")
    print(query)
    # for items in all_blogs:
    # split_items = items.split(" ")
    # print(query, a)
    if len(searched_products) != 0:

        return render(request, "mart/searching.html", {'post': searched_products, "length": len(searched_products)})
    else:
        print("it is reaching here")
        return render(request, "mart/searching.html", {"length": len(searched_products)})


def checkoutc(request):
    if request.method == "POST":
        name = request.POST.get("name")

        address = request.POST.get("address")
        phone = request.POST.get("phone")
        message = request.POST.get("msg")
        items = request.POST.get("itemsJson")
        items = json.loads(items)
        total = len(items)
    print(name, address, phone,message, items)
    orders = order(name=name, address=address, message=message, phone=phone, items=items, total_items=total)
    orders.save()
    # return JsonResponse({"ok": ""}, status=200)
    return render(request,"mart/thanks.html", {'name':name})
#return render(request,"mart/contact.html", {'message': message})
def productpage(request):
    return render(request, "mart/cart.html")