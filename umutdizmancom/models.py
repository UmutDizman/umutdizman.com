from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Inquiry(models.Model):
    class Package(models.TextChoices):
        STARTER = "starter", _("Starter")
        BUSINESS = "business", _("Business")
        PRO = "pro", _("Pro")
        CONSULT = "consult", _("Not sure yet")

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    package = models.CharField(max_length=20, choices=Package.choices, default=Package.CONSULT)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.package})"