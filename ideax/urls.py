from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/logout/', auth_views.logout, name='logout'),

    path('', views.index, name='index'),
    path('idea/list', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/new/', views.idea_new, name='idea_new'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('drafts/', views.idea_draft_list, name='idea_draft_list'),
    path('idea/<int:pk>/publish/', views.idea_publish, name='idea_publish'),
    path('idea/<int:pk>/remove/', views.idea_remove, name='idea_remove'),
    #path('phase/', views.phase_list, name='phase_list'),
    #path('phase/new/', views.phase_new, name='phase_new'),
    #path('phase/<int:pk>/edit/', views.phase_edit, name='phase_edit'),
    #path('phase/<int:pk>/remove/', views.phase_remove, name='phase_remove'),
    path('criterion/', views.criterion_list, name='criterion_list'),
    path('criterion/new/', views.criterion_new, name='criterion_new'),
    path('criterion/<int:pk>/edit/', views.criterion_edit, name='criterion_edit'),
    path('criterion/<int:pk>/remove/', views.criterion_remove, name='criterion_remove'),
    path('idea/<int:pk>/like/', views.like_popular_vote, name='like_ideia'),
    path('idea/<int:pk>/dislike/', views.like_popular_vote, name='dislike_ideia')
]
