from django.shortcuts import render

# функции = вьюхи = контроллеры

def index(request):
    return render(request,'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

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
        ]
    }
    return render(request, 'mainapp/test-context.html', context)