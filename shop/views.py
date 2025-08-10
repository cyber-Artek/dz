from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import ProductForm
from .models import Product, Cart

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url='/')  # редірект якщо не адмін
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            request.session['last_product_id'] = product.id  # збереження в сесію
            return redirect('add_product')
    else:
        form = ProductForm()
    last_product_id = request.session.get('last_product_id')
    last_product = Product.objects.filter(id=last_product_id).first()
    return render(request, 'add_product.html', {
        'form': form,
        'last_product': last_product.name if last_product else 'Немає'
    })

@user_passes_test(is_admin, login_url='/')
def admin_products(request):
    products = Product.objects.all()
    return render(request, 'admin_products.html', {'products': products})

@user_passes_test(is_admin, login_url='/')
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        # Видалити товар з усіх кошиків
        Cart.objects.filter(product_id=pk).delete()
        # Видалити сам товар
        product.delete()
    except Product.DoesNotExist:
        pass
    return redirect('admin_products')

from django.contrib.auth.decorators import login_required

@login_required
def user_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'user_cart.html', {'cart_items': cart_items})


from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Product)
def remove_product_from_cart(sender, instance, **kwargs):
    Cart.objects.filter(product=instance).delete()
