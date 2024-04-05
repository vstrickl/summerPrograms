from django.contrib import admin
from .models import Applicant


# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        'child_first_name',
        'parent_first_name',
        'parent_last_name',
        'phone',
        'email',
        'city',
        'send_email',
        'send_text',
        'need_financial_aid',
    )

admin.site.register(Applicant, ApplicantAdmin)