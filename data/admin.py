from django.contrib import admin
from . models import Staff, PatientVisit, Patient, PatientBill, PatientFeedback
from . models import Drug, Supplier, Appointment, HealthHistory, Prescription

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "position", "shift", "employment_date")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "email", "date_recorded")

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "supply_type", "contract_type", "address")

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ("drug_code", "drug_name", "manufacturer", "supplied_by", "supply_unit", "unit_price", "total_price", "date_recorded")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("patient", "prescribed_by", "prescribed_drug", "prescribed_on", "prescription_notes")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "description", "date_requested", "approved")

@admin.register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_date")

@admin.register(PatientBill)
class PatientBillAdmin(admin.ModelAdmin):
    list_display = ("patient", "treatment_date", "amount", "payment_date")

@admin.register(PatientFeedback)
class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ("patient", "comment", "date_commented")

@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "history")

admin.site.site_title = "CLINIC MANAGEMENT SYSTEM"
admin.site.site_header = "CLINIC MANAGEMENT SYSTEM"






