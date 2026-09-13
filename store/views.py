from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import urllib.parse
from .models import Product, Category, Banner

PHONE_NUMBER = "201003978938"  # اكتب رقم الواتساب بالرمز الدولي بدون +

def product_list(request):
    categories = Category.objects.all()
    banners = Banner.objects.filter(is_active=True).order_by('-created_at')
    
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    
    products = Product.objects.all()
    
    if category_id:
        products = products.filter(category_id=category_id)
        
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
    products = products.order_by('-created_at')
    
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'banners': banners,
        'selected_category': int(category_id) if category_id and category_id.isdigit() else None,
        'query': query or ''
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # جلب منتجين من نفس القسم كمنتجات ذات صلة، أو أي منتجين آخرين لو القسم فاضي
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:2]
    if related_products.count() < 2:
        related_products = Product.objects.exclude(id=product.id)[:2]

    msg = f"السلام عليكم، أحتاج للاستفسار عن المنتج: {product.name}"
    if product.price:
        msg += f" (السعر: {product.price} ج.م)"
    
    product_url = request.build_absolute_uri()
    msg += f"\nرابط المنتج: {product_url}"
    
    encoded_message = urllib.parse.quote(msg)
    whatsapp_url = f"https://wa.me/{PHONE_NUMBER}?text={encoded_message}"
    
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related_products': related_products,
        'whatsapp_url': whatsapp_url,
        'product_url': product_url
    })

def about_us(request):
    return render(request, 'store/about.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ProductForm

def is_staff_user(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff_user, login_url='/admin/login/')
def add_product_custom(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'تمت إضافة المنتج "{product.name}" بنجاح!')
            return redirect('add_product_custom')
    else:
        form = ProductForm()
        
    return render(request, 'store/add_product.html', {'form': form})