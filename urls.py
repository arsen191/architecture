from views import index_view, about_view, contacts_view, ListCategory, CreateCategory, CreateCourse, ListCourses

routes = {
    '/': index_view,
    '/about/': about_view,
    '/contacts/': contacts_view,
    '/categories/': ListCategory(),
    '/create_category/': CreateCategory(),
    '/courses/': ListCourses(),
    '/create_course/': CreateCourse(),
}
