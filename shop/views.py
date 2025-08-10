from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product



products = [
    ("Ноутбук Lenovo", "Потужний ноутбук для роботи", 25000, 5),
    ("Смартфон Samsung", "Новий Galaxy з 256GB пам'яті", 30000, 4),
    ("Навушники Sony", "Безпровідні з шумопоглинанням", 8000, 5),
    ("Клавіатура Logitech", "Механічна з підсвічуванням", 2500, 4),
    ("Монітор LG", "27 дюймів, 144Гц", 7000, 5),
    ("Миша Razer", "Ігрова, RGB", 1800, 4),
    ("Принтер HP", "Лазерний, Wi-Fi", 5500, 4),
    ("Планшет Apple iPad", "256GB, Wi-Fi + Cellular", 35000, 5),
    ("Телевізор Samsung", "55 дюймів, 4K HDR", 22000, 4),
    ("Колонка JBL", "Портативна, водонепроникна", 3000, 5)
]

for p in products:
    Product.objects.create(name=p[0], description=p[1], price=p[2], rating=p[3])


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            response = redirect('add_product')
            response.set_cookie('last_product', product.name, max_age=3600)
            return response
    else:
        form = ProductForm()
    last_product = request.COOKIES.get('last_product', 'Немає')
    return render(request, 'add_product.html', {'form': form, 'last_product': last_product})
