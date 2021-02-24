from django.shortcuts import render

from django.http import HttpResponse
import datetime
# функции = вьюхи = контроллеры

def index(request):
    context = {
        'title': 'geekshop'
    }
    return render(request,'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'geekshop - products',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00', 'img': '/static/vendor/img/products/Adidas-hoodie.png', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00', 'img': '/static/vendor/img/products/Blue-jacket-The-North-Face.png', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00', 'img': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00', 'img': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png', 'description': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00', 'img': '/static/vendor/img/products/Black-Dr-Martens-shoes.png', 'description': 'Гладкий кожаный верх. Натуральный материал'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00', 'img': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ],
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

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
