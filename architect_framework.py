from templator import render


def index_view(request):
    return '200 OK', render('index.html', object_list=[request]).encode('utf-8')


def about_view(request):
    return '200 OK', render('about.html', object_list=[{'lesson': 1}]).encode('utf-8')


def not_found_view(request):
    return '404 NOT FOUND', [b'Not found, please check your address']


routes = {
    '/': index_view,
    '/about/': about_view,
}


def front_controller(request):
    request['fc'] = 'Data to check hw1'


def other_front(request):
    request['fc1'] = 'Another data'


fronts_lst = [front_controller, other_front]


class Application:
    def __init__(self, route, fronts):
        self.routes = route
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        if not path.endswith('/'):
            path += '/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_view
        request = {}
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body


application = Application(routes, fronts_lst)
