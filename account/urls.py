from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

app_name = 'account'

urlpatterns=[
    path('register/', register_view, name="register"),
    path('login/',login_view,name="login"),
    path('logout/', logout_view, name="logout"),

]
