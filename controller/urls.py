from django.urls import path,include
from .views import index, ListMembers, DetailMember, CreateMember, UpdateMember, DeleteMember
from .views import ListDogs, DetailDog, CreateDog, UpdateDog, DeleteDog

app_name = "controller"

urlpatterns = [
    path('',index, name='dashboard'),

    path("member/<int:pk>/",DetailMember.as_view(), name='member-detail'),
    path('member/create/',CreateMember.as_view(), name='member-create'),
    path("member/list/", ListMembers.as_view(), name='member-list'),
    path("member/<int:pk>/update/", UpdateMember.as_view(), name='member-update'),
    path("member/<int:pk>/delete/", DeleteMember.as_view(), name='member-delete'),

    path("dog/<int:pk>/",DetailDog.as_view(), name='dog-detail'),
    path('dog/create/',CreateDog.as_view(), name='dog-create'),
    path("dog/list/", ListDogs.as_view(), name='dog-list'),
    path("dog/<int:pk>/update/", UpdateDog.as_view(), name='dog-update'),
    path("dog/<int:pk>/delete/", DeleteDog.as_view(), name='dog-delete'),



]





