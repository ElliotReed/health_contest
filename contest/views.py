from django.shortcuts import render, redirect
from django.db.models import Sum

from .models import ParticipantContest
from account.models import UserAccount
import json


def index(request):
    user_id = request.user.id
    participant_contests = ParticipantContest.objects.filter(participant=user_id)

    scores = UserAccount.objects.annotate(
        total=Sum("participantcontest__score")
    ).order_by("-total")

    if request.method == "POST":

        for contest in participant_contests:
            data = request.POST.get(contest.contest.name)
            if data:
                score = data
                contest.score = score
                contest.save()
        return redirect("contest:index")

    context = {
        "participant_contests": participant_contests,
        "scores": scores,
    }
    return render(request, "contest/index.html", context)
