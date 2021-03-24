from django.contrib import admin
from django.urls import include, path
from controller.forms import UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',LoginView.as_view(
            template_name="landing.html",
            authentication_form=UserLoginForm,
            redirect_authenticated_user = True)
        , name='landing',
    ),
    path('logout/', LogoutView.as_view(
            next_page = 'landing'

    ), name='logout'),
    path('admin/', admin.site.urls),
    path('controller/',include('controller.urls',namespace="controller"))
]



