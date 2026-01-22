from django.contrib import admin
from .models import (
    Skill, Challenge, ChallengeSubmission,
    UserProfile, Badge, UserBadge, MotivationMessage
)


@admin.register(ChallengeSubmission)
class ChallengeSubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "challenge", "is_approved", "submitted_at")
    list_filter = ("is_approved", "challenge__skill")
    actions = ["approve_submissions"]

    def approve_submissions(self, request, queryset):
        for submission in queryset:
            if not submission.is_approved:
                submission.is_approved = True
                submission.save()

                profile = submission.user.userprofile
                profile.points += submission.challenge.points
                profile.save()

                badge = Badge.objects.filter(name="First Approved Challenge").first()
                if badge:
                    UserBadge.objects.get_or_create(user=submission.user, badge=badge)

    approve_submissions.short_description = "Approve selected submissions"


admin.site.register(Skill)
admin.site.register(Challenge)
admin.site.register(UserProfile)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(MotivationMessage)
