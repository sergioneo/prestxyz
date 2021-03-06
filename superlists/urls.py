from django.conf.urls import url, include
from lists import views as list_views
from lists import urls as list_urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^admin/', include(admin.site.urls)),
]