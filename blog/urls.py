from django.urls import path
from django.contrib.auth import logout
from django.shortcuts import redirect
from .views.auth_view import register, login
from .views.main_view import home,create_blog, single_blog, edit_blog, delete_blog

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

urlpatterns = [
    path("",home, name="home"),
    path("register/",register, name="register"),
    path("login/",login, name ="login"),
    path("create/",create_blog),
    path("<int:blog_id>",single_blog, name="blog_detail"),
    path("<int:blog_id>/edit/", edit_blog, name="edit_blog"),
    path("<int:blog_id>/delete",delete_blog,name="delete_blog"),
    path("logout/", logout_view, name="logout"),  # Add logout path
]

