def front_controller(request):
    request['fc'] = 'Data to check hw1'


def other_front(request):
    request['fc1'] = 'Another data'


fronts_lst = [front_controller, other_front]