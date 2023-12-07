from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_members, name='team_members'),
    path('add_member/', views.add_member, name='add_member'),
    path('edit_member/<int:member_id>/ ', views.edit_member, name='edit_member'),
]