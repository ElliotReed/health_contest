from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

from account.models import UserAccount


class ContestType(models.Model):
    contest_type = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.contest_type


class Contest(models.Model):
    name = models.CharField(blank=True, max_length=150)
    contest_type = models.ForeignKey(ContestType, on_delete=PROTECT)

    def __str__(self):
        return self.name


class ParticipantContest(models.Model):
    contest = models.ForeignKey(Contest, on_delete=CASCADE)
    participant = models.ForeignKey(UserAccount, on_delete=CASCADE)
    description = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.contest.name}, {self.participant.username}"


class WeeklyScore(models.Model):
    weekly_score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(UserAccount, on_delete=CASCADE)

    def __str__(self):
        return self.weekly_score
