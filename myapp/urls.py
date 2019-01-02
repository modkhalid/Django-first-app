from django.conf.urls import url
from . import views

app_name="my_app"
urlpatterns=[
    url(r'^$',views.home,name="home"),
    url(r'^register/$',views.registration,name="registration"),
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^special/$',views.special,name="special")
]
