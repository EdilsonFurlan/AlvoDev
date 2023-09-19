
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matprima/',include('mat_prima.urls')),
    path('',include('mat_prima.urls'))
]
