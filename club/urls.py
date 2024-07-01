from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('schedule/<int:year>/<int:month>/', views.schedule_list, name='schedule_list'),
    path('schedule/add/', views.schedule_create, name='schedule_add'),
    path('schedule/update/<int:pk>/', views.schedule_update, name='schedule_update'),
    path('schedule/delete/<int:pk>/', views.schedule_delete, name='schedule_delete'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/add/', views.dashboard_create, name='dashboard_add'),
    path('dashboard/update/<int:pk>/', views.dashboard_update, name='dashboard_update'),
    path('dashboard/delete/<int:pk>/', views.dashboard_delete, name='dashboard_delete'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/add/', views.post_create, name='post_add'),
    path('posts/detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/update/<int:pk>/', views.post_update, name='post_update'),
    path('posts/delete/<int:pk>/', views.post_delete, name='post_delete'),
]
