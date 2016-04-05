from django.conf.urls import url
import views


urlpatterns = [
    #url
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail)
]