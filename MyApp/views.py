from django.shortcuts import render
from django.http import HttpResponse

USER_DATA = {    
    'first_name': 'Иван',    'middle_name':'Петрович',    
    'last_name': 'Иванов',    
    'phone': '8-923-600-01-02',    
    'email': 'vasya@mail.ru'
    }
items = [    
    {"id": 1, "name": "Кроссовки Adidas","quantity": 5},    
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},   
    {"id": 3, "name": "Coca-Cola 1 литр", "quantity": 3},    
    {"id": 4, "name": "Картофель фри", "quantity": 4},    
    {"id": 5, "name": "Кепка", "quantity": 1},
    ]

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
        item = next((item for item in items if item["id"] == int(item_id)), None)
        if not item:
            raise ValueError("Товар не найден")
        
        context = {'item': item}
        return render(request, 'item.html', context)
    except Exception as e:
        return HttpResponse(f"{e}", status=404)
    

def item_list(request):
    context = {'items': items}
    return render(request, 'item_list.html', context)