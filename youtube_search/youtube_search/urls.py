from django.conf.urls import include, url
from django.contrib import admin
from webapp import views as webview

urlpatterns = [
    # Examples:
    # url(r'^$', 'youtube_search.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', webview.VideoList,name='videolist'),
    url(r'^video_list/$', webview.RestApiList,name='restapilist'),
    url(r'^video_list/(?P<pk>[a-zA-Z0-9._-]+)/$', webview.VideoDetail,name='videodetail'),
]
