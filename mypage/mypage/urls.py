from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('todolist/', include('todolist.urls')),
    path('admin/', admin.site.urls),
]