from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

from account.models import UserAccount


class ContestType(models.Model):
    contest_type = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.contest_type


class Contest(models.Model):
    name = models.CharField(blank=True, max_length=150)
    # duration
    prize = models.CharField(max_length=255, null=True, blank=True)
    contest_type = models.ForeignKey(ContestType, on_delete=PROTECT)

    def __str__(self):
        return self.name


class ScoreMethod(models.Model):
    method = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return self.method


class ContestRules(models.Model):
    contest = models.ForeignKey(Contest, on_delete=PROTECT)
    rule = models.CharField(blank=True, max_length=150)
    score_method = models.ForeignKey(ScoreMethod, on_delete=CASCADE)

    def __str__(self):
        return self.rule


class ParticipantContest(models.Model):
    contest = models.ForeignKey(Contest, on_delete=CASCADE)
    participant = models.ForeignKey(UserAccount, on_delete=CASCADE)
    description = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.contest.name}, {self.participant.username}"


class ContestRound(models.Model):
    contest = models.ForeignKey(Contest, on_delete=PROTECT)
    participant = models.ForeignKey(UserAccount, on_delete=CASCADE)

    def __str__(self):
        return self.contest.name
