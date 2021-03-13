from django.contrib import admin
from django.urls import include, path
from controller.views import landing



urlpatterns = [
    path('',landing, name="landing"),
    path('admin/', admin.site.urls),
    path('controller/',include('controller.urls',namespace="controller"))
]

