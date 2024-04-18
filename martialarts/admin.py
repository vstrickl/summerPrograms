from django.contrib import admin
from .models import FinancialAidApplicant


# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        'child_first_name',
        'parent_first_name',
        'parent_last_name',
        'household_income',
        'phone',
        'email',
        'city',
        'send_email',
        'send_text',
        'aid_awarded'
    )

admin.site.register(FinancialAidApplicant, ApplicantAdmin)