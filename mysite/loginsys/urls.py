from django.conf.urls import url,include
from . import views

app_name = 'auth'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^register/$',views.register,name='register')
]