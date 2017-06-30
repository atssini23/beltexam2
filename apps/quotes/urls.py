from django.conf.urls import url
from.import views

app_name = 'quotes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addquote$', views.addquote, name='addquote'),
    # url(r'^users/(?P<id>\d+)$', views.detail, name='details'),
    url(r'^addLike$', views.addLike, name='addLike'),
]
