from django.contrib import admin

from .models import (
    Contest,
    ContestRound,
    ContestRules,
    ContestType,
    ParticipantContest,
    ScoreMethod,
)


class ParticipantContestAdmin(admin.ModelAdmin):
    list_display = ("get_contest", "get_user", "updated_at")

    @admin.display(description="contest")
    def get_contest(self, obj):
        return obj.contest.name

    @admin.display(description="participant")
    def get_user(self, obj):
        return obj.participant.username

    get_contest.admin_order_field = "contest__name"
    get_user.admin_order_field = "participant__username"


admin.site.register(Contest)
admin.site.register(ContestRound)
admin.site.register(ContestRules)
admin.site.register(ContestType)
admin.site.register(ParticipantContest, ParticipantContestAdmin)
admin.site.register(ScoreMethod)
