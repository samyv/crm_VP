from django.urls import path,include
from .views import index, create_member, member_detail, list_members, update_member, delete_member


url_members = [
    path("<int:pk>/",member_detail),
    path('create/',create_member),
    path("list/", list_members),
    path("<int:pk>/update/", update_member),
    path("<int:pk>/delete/", delete_member),
]

app_name = "member"



urlpatterns = [
    path('',index, name='index'),
    path('member/',include(url_members))
]





