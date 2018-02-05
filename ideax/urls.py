from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/new/', views.idea_new, name='idea_new'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('drafts/', views.idea_draft_list, name='idea_draft_list'),
    path('idea/<int:pk>/publish/', views.idea_publish, name='idea_publish'),
    path('idea/<int:pk>/remove/', views.idea_remove, name='idea_remove'),
]
