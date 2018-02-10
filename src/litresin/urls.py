from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, LitresinCBView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', LitresinCBView.as_view(), name='scode'), 
]