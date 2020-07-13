from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('structure/', include('api.structure.urls')),
    path('users/', include('api.users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
