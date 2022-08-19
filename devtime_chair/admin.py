from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Record

# Register your models here.
admin.site.register(Record)

admin.site.unregister(User)
admin.site.unregister(Group)