from django.db import models

# Create your models here.
class FinancialAidApplicant(models.Model):
    parent_first_name = models.CharField(null=True, blank=True)
    parent_last_name = models.CharField(null=True, blank=True)
    child_first_name = models.CharField(null=True, blank=True)
    child_last_name = models.CharField(null=True, blank=True)
    story = models.TextField(null=True, blank=True, verbose_name="How will training Martial Arts Improve your child's life?")
    street_address = models.CharField(null=True, blank=True)
    city = models.CharField(null=True, blank=True)
    state = models.CharField(null=True, blank=True)
    zip_code = models.CharField(null=True, blank=True)
    email = models.CharField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    send_email = models.BooleanField(null=True, blank=True)
    send_text = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.child_first_name} {self.child_last_name}'