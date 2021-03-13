from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dog, Member, Address, Race

# admin.site.register(User)
admin.site.register(Member)
admin.site.register(Dog)
admin.site.register(Address)
admin.site.register(Race)
