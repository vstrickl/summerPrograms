from django.db import models

# Create your models here.
class Applicant(models.Model):
    parent_first_name = models.CharField(null=True, blank=True)
    parent_last_name = models.CharField(null=True, blank=True)
    child_first_name = models.CharField(null=True, blank=True)
    child_last_name = models.CharField(null=True, blank=True)
    street_address = models.CharField(null=True, blank=True)
    city = models.CharField(null=True, blank=True)
    state = models.CharField(null=True, blank=True)
    zip_code = models.CharField(null=True, blank=True)
    email = models.CharField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    send_email = models.BooleanField(null=True, blank=True)
    send_text = models.BooleanField(null=True, blank=True)
    need_financial_aid = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.child_first_name} {self.child_last_name}'