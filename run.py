from wsgiref.simple_server import make_server
from architect_framework import Application
from urls import routes
from front_controller import fronts_lst

app = Application(routes, fronts_lst)

with make_server('', 8000, app) as server:
    print('Запуск сервера...')
    server.serve_forever()
