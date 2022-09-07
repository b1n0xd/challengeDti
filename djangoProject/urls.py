from django.contrib import admin
from django.urls import path, include # novo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')), # novo
]