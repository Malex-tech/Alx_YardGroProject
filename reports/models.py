from django.db import models
from django.conf import settings

class Report(models.Model):
    REPORT_TYPES = (
        ('delivery', 'Delivery'),
        ('wastage', 'Wastage'),
        ('general', 'General'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} report by {self.user.username}"
