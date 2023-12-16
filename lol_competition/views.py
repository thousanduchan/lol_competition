from django.shortcuts import render, redirect
from team.models import Team


def index(request):
    if request.method == 'POST':
        data_post = request.POST

        obj_team = Team.objects.get(id=data_post['team_id'])
        context = {'obj_team': obj_team}

        return render(request, 'victory.html', context)

    obj_team = Team.objects.all().order_by('-score')

    context = {'obj_team': obj_team}
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        data_post = request.POST

        members_list = data_post['member1'] + '\n' + data_post['member2'] + '\n' + data_post['member3'] + '\n' + data_post['member4'] + '\n' + data_post['member5']

        Team.objects.create(
            name=data_post['team_name'],
            members=members_list,
            image=request.FILES.get('image'),
            score=0,
        )

        return redirect('home')

    return render(request, 'register.html')


def control_score(request, team_id):
    if request.method == 'POST':
        data_post = request.POST

        obj_team = Team.objects.get(id=team_id)

        obj_team.score += int(data_post['control'])
        if obj_team.score < 0:
            obj_team.score = 0

        obj_team.save()

    return redirect('home')


def delete_team(request, team_id):
    if request.method == 'POST':
        obj_team = Team.objects.get(id=team_id)
        obj_team.delete()

    return redirect('home')
