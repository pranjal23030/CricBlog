from django.urls import path
from .views.auth_view import register, login
from .views.main_view import home,create_blog, single_blog, edit_blog


urlpatterns = [
    path("",home, name="home"),
    path("register/",register, name="register"),
    path("login/",login, name ="login"),
    path("create/",create_blog),
    path("single/",single_blog),
    path("edit/",edit_blog)

]

