from django.contrib import admin
from django.urls import path
from IDsender import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.no,name ="no"),
    path("ig/",views.ig,name ="ig"),
]
