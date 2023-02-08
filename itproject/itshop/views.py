from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from.models import Product,Category

# Create your views here
# def home(request):
#     return render(request,'itshop/index.html')

class home(View):
    def post(self,request):
        pass
    def get(self,request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
        # p= Product.get_all_products()
        # cat=Category.get_all_categories()


        products = None
        categories = Category.get_all_categories()
        CategoryID = request.GET.get('category')


        if CategoryID:
            products = Product.get_products_by_category_id(CategoryID)
        else:
            products = Product.get_all_products()
        
        data={}
        data['products']=products
        data['cat']=categories
        
        return render(request,'itshop/index.html',data)