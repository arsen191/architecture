from templator import render


def index_view(request):
    return '200 OK', render('index.html', object_list=[request]).encode('utf-8')


def about_view(request):
    return '200 OK', render('about.html', object_list=[{'lesson': 1}]).encode('utf-8')


def contacts_view(request):
    return '200 OK', render('contacts.html', object_list=[{'test': 'test'}]).encode('utf-8')


def not_found_view(request):
    return '404 NOT FOUND', [b'Not found, please check your address']
