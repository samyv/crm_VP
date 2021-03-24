from django.urls import path,include
from .views import index, ListMembers, DetailMember, CreateMember, UpdateMember, DeleteMember

app_name = "controller"

urlpatterns = [
    path('',index, name='index'),
    path("member/<int:pk>/",DetailMember.as_view(), name='member-detail'),
    path('member/create/',CreateMember.as_view(), name='member-create'),
    path("member/list/", ListMembers.as_view(), name='member-list'),
    path("member/<int:pk>/update/", UpdateMember.as_view(), name='member-update'),
    path("member/<int:pk>/delete/", DeleteMember.as_view(), name='member-delete'),
]





