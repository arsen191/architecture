from templator import render
from patterns.creational_patterns import Engine, Logger

log = Logger('abc')
log1 = Logger('abc1')
site = Engine()


def index_view(request):
    return '200 OK', render('index.html', object_list=[{'title': 'Главная', 'advert': 'здесь могла бы быть ваша реклама'}])


def about_view(request):
    return '200 OK', render('about.html', object_list=[{'lesson': 3, 'title': 'О нас'}])


def contacts_view(request):
    return '200 OK', render('contacts.html', object_list=[{'test': 'test', 'title': 'Контакты'}])


def not_found_view(request):
    return '404 NOT FOUND', [b'Not found, please check your address']


class CreateCategory:
    def __call__(self, request):
        if request['REQUEST_METHOD'] == 'POST':
            site.create_category(request['data']['name'])
            return '200 OK', render('categories.html', object_list=site.categories)
        return '200 OK', render('create_category.html', object_list=site.list_categories())


class ListCategory:
    def __call__(self, *args, **kwargs):
        log.logging('zxc')
        categories = site.list_categories()
        return '200 OK', render('categories.html', object_list=categories)


class CreateCourse:
    def __call__(self, request):
        if request['REQUEST_METHOD'] == 'POST':
            site.create_course('online', request['data']['name'])
            return '200 OK', render('courses.html', object_list=site.list_courses())
        return '200 OK', render('create_course.html', object_list=site.list_courses())


class ListCourses:
    def __call__(self, *args, **kwargs):
        courses = site.list_courses()
        return '200 OK', render('courses.html', object_list=courses)
