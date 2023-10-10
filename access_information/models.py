from django.db import models

class GameBox(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    challenge_id = models.PositiveIntegerField(null=True, blank=True)
    team_id = models.PositiveIntegerField(null=True, blank=True)
    ip = models.CharField(max_length=255, null=True, blank=True)
    port = models.CharField(max_length=255, null=True, blank=True)
    ssh_port = models.CharField(max_length=255, null=True, blank=True)
    ssh_user = models.CharField(max_length=255, null=True, blank=True)
    ssh_password = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    visible = models.BooleanField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    is_down = models.BooleanField(null=True, blank=True)
    is_attacked = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'game_boxes'
