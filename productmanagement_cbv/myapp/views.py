from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from myapp.models import Product
from myapp.forms import ProductForm


def home(request):
    return render(request,'myapp/home.html')

class ProductAPI(View):
    def get(self,request,id=None):
        if id:
            product = Product.objects.filter(id=id).values('id','name','price').first()
            if not product:
                return JsonResponse({'error':'Productnot found'}, status=404)
            return JsonResponse(product)
        else:
            products = list(Product.objects.values('id','name','price'))
            return JsonResponse(products,safe=False)
    
    def post(self,request):
        data = json.loads(request.body)
        form = ProductForm(data)
        if form.is_valid():
            product = form.save()
            return JsonResponse({'id':product.id, 'name':product.name,'price':product.price})
        else:
            return JsonResponse(form.errors,status=400)
        
    def put(self,request,id):
        data = json.loads(request.body)
        product = Product.objects.get(id=id)
        form = ProductForm(data , instance=product)
        if form.is_valid():
            product.save()
            return JsonResponse({'id':product.id, 'name':product.name,'price':product.price})
        else:
            return JsonResponse(form.errors,status=400)
    def delete(self,request,id):
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse({'message':'Product deleted successfully!'})
    
def product_detail_view(request,id):
    return render(request , 'myapp/product_detail.html')