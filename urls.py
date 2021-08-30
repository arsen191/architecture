from views import index_view, about_view, contacts_view

routes = {
    '/': index_view,
    '/about/': about_view,
    '/contacts/': contacts_view
}