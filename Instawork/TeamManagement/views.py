from django.shortcuts import render, redirect
from .models import TeamMember
from .forms import TeamMemberForm


def team_members(request):
    members = TeamMember.objects.all()
    return render(request, 'team_members.html', {'members': members})


def add_member(request):
    if request.method == "POST":
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_members')
    else:
        form = TeamMemberForm()
    return render(request, 'add_member.html', {'form': form})


def edit_member(request, member_id):

    member = TeamMember.objects.get(id=member_id)
    if request.method == "POST":
        if request.POST.get('action') == 'delete':
            member.delete()

        else: 
            form = TeamMemberForm(request.POST, instance=member)
            if form.is_valid():
                form.save()        
        return redirect('team_members')  
    else:
        form = TeamMemberForm(instance=member)

    return render(request, 'edit_member.html', {'form': form})
