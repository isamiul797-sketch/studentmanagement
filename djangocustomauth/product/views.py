from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import permission_required
from product.models import Product
from product.forms import ProductForm

# Create your views here.

@permission_required('product.view_product', raise_exception=True)
def product_list(request):
    products = Product.objects.all()
    return render(request,'product/list.html',{'products':products})

@permission_required('product.view_product', raise_exception=True)
def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,'product/detail.html',{'product':product})

@permission_required('product.add_product', raise_exception=True)
def product_add(request):
    if request.method == "POST":
        form = Product(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
  
    return render(request,'product/add.html',{'form':form})

@permission_required('product.change_product', raise_exception=True)
def product_edit(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request,'product/add.html',{'form':form})

@permission_required('product.delete_product', raise_exception=True)
def product_delete(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == "POST":
            product.delete()
            return redirect('product_list')
    return render(request,'product/delete.html',{'product':product})