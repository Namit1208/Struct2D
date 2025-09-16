from django.db import models

# Optional: save scenarios later
class Scenario(models.Model):
    title = models.CharField(max_length=120)
    ds = models.CharField(max_length=16)  # stack|queue|list|bst|avl|heap
    data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

