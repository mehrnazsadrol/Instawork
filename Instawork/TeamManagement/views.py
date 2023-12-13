from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import TeamMember
from .forms import TeamMemberForm


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_members.html'
    context_object_name = 'members'


"""
View for creating a team member.

"""


class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'add_member.html'
    success_url = reverse_lazy('team_members')


"""
View for updating a team member's information.

Methods:
    post(request, *args, **kwargs): Handles the POST request for updating the team member.
"""


class TeamMemberUpdateView(UpdateView):

    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'edit_member.html'
    success_url = reverse_lazy('team_members')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.POST.get('action') == 'delete':
            self.object.delete()
            return redirect(self.success_url)
        else:
            return super(TeamMemberUpdateView, self).post(request, *args, **kwargs)
