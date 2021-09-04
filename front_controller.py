def front_controller(request, env, data):
    request.update(env)
    request['data'] = data


fronts_lst = [front_controller]
