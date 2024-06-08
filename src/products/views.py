from django.http import Http404
from django.shortcuts import render, redirect
from .models import CategoryModel, ProductForm, ProductModel
from django.contrib.auth.decorators import login_required, permission_required

# Sales view:
def sales(request):
    context = { "active": "sales" }
    return render(request, "sales.html", context)

#Products view:
def list(request):
    products = ProductModel.objects.all()
    context = { "active": "products", "products": products }
    return render(request, "products.html", context)

#Details view:
def details(request, id):
    try:
        product = ProductModel.objects.get(pk = id) #pk Primary key
        context = { "product": product }
        return render(request, "details.html", context)
    except ProductModel.DoesNotExist:
        raise Http404()

#Category view:
def categories(request):
    categories = CategoryModel.objects.all()
    context = { "active": "categories", "categories": categories }
    return render(request, "categories.html", context)

#Insert view
@login_required(login_url= "login")
def insert(request):
    if request.method == "GET":
        context = { "active": "insert", "form": ProductForm()}
        return render(request, "insert.html", context)
    
    form = ProductForm(request.POST)
    if not form.is_valid(): # returns true if all is valid or False if there are validations errors
        context = {"form": form}
        return render(request, "insert.html", context)
    form.save() # save in database
    return redirect("products")

# Edit View:
@login_required(login_url= "login")
def edit(request, id):
    try:
        if request.method == "GET":
            product = ProductModel.objects.get(pk = id)
            context = { "form": ProductForm(instance=product) }
            return render(request, "edit.html", context)
        
        dummy_product = ProductModel(pk = id)
        form = ProductForm(request.POST, instance=dummy_product)
        if not form.is_valid():
            context = { "form":form }
            return render(request, "edit.html", context)
        form.save() # save in database
        return redirect("products")
    except ProductModel.DoesNotExist:
        raise Http404()

# Delete View:
@permission_required("is_superuser", login_url= "login")
def delete(request, id):
    try:
        dummy_product = ProductModel(pk = id)
        dummy_product.delete()
        return redirect("products")
    except ProductModel.DoesNotExist:
        raise Http404()
 
# Info view:
def info(request):
    context = { "active": "info" }
    return render(request, "info.html", context)
