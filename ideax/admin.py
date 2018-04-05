from django.contrib import admin
from .models import Idea, UserProfile, Popular_Vote, Comment

admin.site.register(Idea)
admin.site.register(UserProfile)
admin.site.register(Popular_Vote)
admin.site.register(Comment)
