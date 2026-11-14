from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'ProductApplication/index.html'
    context_object_name = 'products'

def login(request):
    result=""
    try:
        username = request.GET['txtusr']
        password = request.GET['txtpass']
        if(username == "admin" and password == "12345"):
            result="Login successful!"
        else:
            result="Login Failed"
    except Exception as e:
        print(e)
    return render(request,"ProductApplication/login.html",{'result':result})

def insert(request):
    result=""
    try:
        id = request.GET['txtid']
        name = request.GET['txtname']
        description = request.GET['txtdesc']
        price = request.GET['txtprice']
        Product.objects.create(id=id, name=name, description=description, price=price)
        result="Product inserted successfully!"
    except Exception as e:
        print(e)
    return render(request,"ProductApplication/insert.html",{'result':result})

def update(request):
    result=""
    try:
        id = request.GET['txtid']
        name = request.GET['txtname']
        description = request.GET['txtdesc']
        price = request.GET['txtprice']
        Product.objects.filter(id=id).update(name=name, description=description, price=price)
        result="Product updated successfully!"
    except Exception as e:
        print(e)
    return render(request,"ProductApplication/update.html",{'result':result})

def delete(request):
    result=""
    try:
        id = request.GET['txtid']
        Product.objects.filter(id=id).delete()
        result="Product deleted successfully!"
    except Exception as e:
        print(e)
    return render(request,"ProductApplication/delete.html",{'result':result})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'ProductApplication/prodetails.html'
    context_object_name = 'product'



def custdetails(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ProductApplication/custdetails.html', {'product': product})


class OrderDetailView(DetailView):
    model = Product
    template_name = 'ProductApplication/order.html'
    context_object_name = 'product'
    

        








