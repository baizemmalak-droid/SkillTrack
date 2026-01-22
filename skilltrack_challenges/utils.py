from .models import ChallengeSubmission


def can_access_challenge(user, challenge):
    if challenge.level == "easy":
        return True

    if challenge.level == "intermediate":
        return ChallengeSubmission.objects.filter(
            user=user,
            challenge__skill=challenge.skill,
            challenge__level="easy",
            is_approved=True
        ).exists()

    if challenge.level == "advanced":
        return ChallengeSubmission.objects.filter(
            user=user,
            challenge__skill=challenge.skill,
            challenge__level="intermediate",
            is_approved=True
        ).exists()

    return True



