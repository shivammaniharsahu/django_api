from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'login_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('admin/', admin.site.urls),
    url('', include('workshop.urls')),
    url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
]

