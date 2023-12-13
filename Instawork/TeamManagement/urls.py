from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView

urlpatterns = [
    path('team/', TeamMemberListView.as_view(), name='team_members'),
    path('team/add/', TeamMemberCreateView.as_view(), name='add_member'),
    path('team/edit/<int:pk>/', TeamMemberUpdateView.as_view(), name='edit_member'),
]
