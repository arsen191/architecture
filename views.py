from templator import render


def index_view(request):
    return '200 OK', render('index.html', object_list=[{'title': 'Главная', 'advert': 'здесь могла бы быть ваша реклама'}]).encode('utf-8')


def about_view(request):
    return '200 OK', render('about.html', object_list=[{'lesson': 3, 'title': 'О нас'}]).encode('utf-8')


def contacts_view(request):
    return '200 OK', render('contacts.html', object_list=[{'test': 'test', 'title': 'Контакты'}]).encode('utf-8')


def not_found_view(request):
    return '404 NOT FOUND', [b'Not found, please check your address']
