from django.apps import AppConfig

class SkilltrackChallengesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skilltrack_challenges'

    def ready(self):
        import skilltrack_challenges.signals

  
