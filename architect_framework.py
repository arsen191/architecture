import quopri
from front_controller import fronts_lst
from views import not_found_view
from urls import routes


class Application:
    def __init__(self, route, fronts):
        self.routes = route
        self.fronts = fronts

    def __call__(self, environ, start_response):
        data = None
        path = environ.get('PATH_INFO')
        query_string = environ.get('QUERY_STRING')
        request_method = environ.get('REQUEST_METHOD')
        if request_method == 'GET':
            data = Application.parse_params(query_string)
        elif request_method == 'POST':
            post_data = Application.get_post_data(environ)
            data = Application.parse_post_data(post_data)
        if not path.endswith('/'):
            path += '/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_view
        request = {}
        for front in self.fronts:
            front(request, environ, data)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def parse_params(query):
        result = {}
        if query:
            splited_lst = query.split('&')
            for el in splited_lst:
                k, v = el.split('=')
                result[k] = v
            return result

    @staticmethod
    def get_post_data(env):
        content_length = env.get('CONTENT_LENGTH')
        content_length = int(content_length) if content_length else 0
        result = env.get('wsgi.input').read(content_length) if content_length else b''
        return result

    @staticmethod
    def parse_post_data(data: bytes):
        result = {}
        if data:
            raw_result = Application.parse_params(data.decode('utf-8'))
            result = Application.decode_value(raw_result)
        return result

    @staticmethod
    def decode_value(data: dict):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace('+', ' '), 'utf-8')
            val_decode_str = quopri.decodestring(val).decode('utf-8')
            new_data[k] = val_decode_str
        return new_data


application = Application(routes, fronts_lst)
