from django.contrib import admin
from .models import Inquiry
# Register your models here.



@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "package", "created_at", "is_contacted")
    list_filter = ("package", "is_contacted", "created_at")
    search_fields = ("name", "email", "phone", "message")