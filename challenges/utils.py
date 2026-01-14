from django.utils import timezone
from .models import UserChallenge, UserBadge, Badge

def get_total_points(user):
    completed = UserChallenge.objects.filter(user=user, completed=True)
    return sum(uc.challenge.points for uc in completed)


def get_level(points):
    if points < 50:
        return "Beginner"
    elif points < 150:
        return "Intermediate"
    elif points < 300:
        return "Advanced"
    return "Expert"


def award_badges(user):
    points = get_total_points(user)
    completed_count = UserChallenge.objects.filter(user=user, completed=True).count()

    badges = []

    if completed_count >= 1:
        badges.append("First Challenge")
    if completed_count >= 5:
        badges.append("5 Challenges")
    if points >= 100:
        badges.append("100 Points")

    for badge_name in badges:
        badge, _ = Badge.objects.get_or_create(
            name=badge_name,
            defaults={"description": badge_name}
        )
        UserBadge.objects.get_or_create(user=user, badge=badge)
