from django.contrib import admin
from .models import Idea, UserProfile, Popular_Vote, Comment, Category, Dimension, Category_Dimension, Evaluation, Category_Image, Use_Term

admin.site.register(Idea)
admin.site.register(UserProfile)
admin.site.register(Popular_Vote)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Dimension)
admin.site.register(Category_Dimension)
admin.site.register(Evaluation)
admin.site.register(Category_Image)
admin.site.register(Use_Term)
