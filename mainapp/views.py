from django.shortcuts import render
import datetime
from mainapp.models import Product, ProductCategory

# функции = вьюхи = контроллеры

def index(request):
    context = {
        'title': 'geekshop'
    }
    return render(request,'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'geekshop - products',
        # 'products': [
        #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00', 'img': 'vendor/img/products/Adidas-hoodie.png', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
        #     {'name': 'Синяя куртка The North Face', 'price': '23 725,00', 'img': 'vendor/img/products/Blue-jacket-The-North-Face.png', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
        #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00', 'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
        #     {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00', 'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png', 'description': 'Плотная ткань. Легкий материал.'},
        #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00', 'img': 'vendor/img/products/Black-Dr-Martens-shoes.png', 'description': 'Гладкий кожаный верх. Натуральный материал'},
        #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00', 'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        # ],
        'products': Product.objects.all(),
        'categories':ProductCategory.objects.all(),
        'now': datetime.datetime.now(),
    }
    return render(request, 'mainapp/products.html', context)

def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00'},
        ],
    }
    return render(request, 'mainapp/test-context.html', context)