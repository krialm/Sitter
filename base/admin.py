from django.contrib import admin

from .models import Room, Message, Topic, User

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(User)