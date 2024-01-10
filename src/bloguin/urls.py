from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
