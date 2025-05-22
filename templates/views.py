from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

USER_DATA = {
    'first_name': 'Иван',
    'middle_name': 'Петрович',
    'last_name': 'Иванов',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
}

def test(request):
    return render(request, 'test_page.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    html_content = f"""
    <p>Имя: {USER_DATA['first_name']}<br>
    Отчество: {USER_DATA['middle_name']}<br>
    Фамилия: {USER_DATA['last_name']}<br>
    Телефон: {USER_DATA['phone']}<br>
    Email: {USER_DATA['email']}</p>
    """

    back_link = '<p><a href="/">Вернуться на главную страницу</a></p>'

    return HttpResponse(html_content + back_link)

def show_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        return render(request, 'item.html', {'item': item})
    except Item.DoesNotExist:
        return HttpResponse("Товар не найден.", status=404)

def item_list(request):
    items = Item.objects.all().order_by('id')  # получаем все товары и сортируем по id
    context = {
        'items': items,
    }
    return render(request, 'item_list.html', context)