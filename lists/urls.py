from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name = "view_list"),
    url(r'^(\d+)/add_item$', views.add_item, name = "add_item"),
    url(r'^(\d+)/items/(\d+)/check', views.check_item, name = "check_item"),
    url(r'^(\d+)/update_title', views.update_title, name = "update_title"),
]
