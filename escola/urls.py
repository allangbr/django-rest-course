from django.contrib import admin
from django.urls import path, include
from cursos.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('cursos.urls'), name='cursos'),
    path('api/v2/', include(router.urls), name='router'),
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
]
