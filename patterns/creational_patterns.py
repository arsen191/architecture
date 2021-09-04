class Course:
    def __init__(self, name):
        self.name = name


class Online(Course):
    pass


class Offline(Course):
    pass


class CourseFactory:
    course_types = {
        'online': Online,
        'offline': Offline
    }

    @classmethod
    def fabric_method_create(cls, course_type, name):
        return cls.course_types[course_type](name)


class Category:
    pk = 0

    def __init__(self, name):
        self.id = Category.pk
        Category.pk += 1
        self.name = name


class Engine:
    def __init__(self):
        self.categories = []
        self.courses = []

    def create_category(self, name):
        self.categories.append(Category(name))

    def list_categories(self):
        if self.categories:
            return self.categories
        return [{'name': 'No categories yet'}]

    def create_course(self, type_, name):
        self.courses.append(CourseFactory.fabric_method_create(type_, name))

    def list_courses(self):
        if self.courses:
            return self.courses
        return [{'name': 'No courses yet'}]


class Singletone(type):
    _instances = {}

    def __call__(cls, name):
        if name not in cls._instances:
            cls._instances[name] = super(Singletone, cls).__call__(name)
        return cls._instances[name]


class Logger(metaclass=Singletone):
    def __init__(self, log_name):
        self.log_name = log_name

    def logging(self, log):
        print(f'Записан лог: {log}')


