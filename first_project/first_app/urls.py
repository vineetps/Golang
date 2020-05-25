from django.conf.urls import url
# from django.contrib import admin
from first_app import views

# for referene URL
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]