from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), #regex post wil be a number, assigned it a view called posts_list
]