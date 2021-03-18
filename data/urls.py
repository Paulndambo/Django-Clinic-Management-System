from django.urls import path
from . import views

urlpatterns = [
    #Viewing data
    path("", views.index, name="index"),
    path("patients/", views.patients, name="patients"),
    path("staff/", views.staffs, name="staff"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("prescriptions/", views.prescriptions, name="prescriptions"),
    path("drugs/", views.drugs, name="drugs"),
    path("feedbacks/", views.feedback, name="feedbacks"),
    path("health_histories/", views.health_histories, name="health_histories"),
    path("appointments/", views.appointments, name="appointments"),
    path("bills/", views.bills, name="bills"),
    path("visits/", views.visits, name="visits"),

    #Inserting Data
    path("add_appointment/", views.add_appointment, name="add_appointment"),
    path("add_bill/", views.add_bill, name="add_bill"),
    path("add_drug/", views.add_drug, name="add_drug"),
    path("add_feedback/", views.add_feedback, name="add_feedback"),
    path("add_health_history/", views.add_health_history, name="add_health_history"),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("add_prescription/", views.add_prescription, name="add_prescription"),
    path("add_staff/", views.add_staff, name="add_staff"),
    path("add_supplier/", views.add_supplier, name="add_supplier"),
    path("add_visit/", views.add_visit, name="add_visit"),

    #Viewing Details
    path("supplier_details/<int:id>/", views.supplier_details, name="supplier_details"),
    path("patient_details/<int:id>/", views.patient_details, name="patient_details"),
    path("prescription_details/<int:id>/", views.prescription_details, name="prescription_details"),
    path("staff_details/<int:id>/", views.staff_details, name="staff_details"),
    path("drug_details/<int:id>/", views.drug_details, name="drug_details"),
    path("appointment_details/<int:id>/", views.appointment_details, name="appointment_details"),

    #Editing Details
    path("edit_appointment/<int:id>/", views.add_appointment, name="edit_appointment"),
    path("edit_bill/<int:id>/", views.add_bill, name="edit_bill"),
    path("edit_drug/<int:id>/", views.add_drug, name="edit_drug"),
    path("edit_patient/<int:id>/", views.add_patient, name="edit_patient"),
    path("edit_health_history/<int:id>/", views.add_health_history, name="edit_health_history"),
    path("edit_staff/<int:id>/", views.add_staff, name="edit_staff"),
    path("edit_supplier/<int:id>/", views.add_supplier, name="edit_supplier"),
    path("edit_visit/<int:id>/", views.add_visit, name="edit_visit"),
    path("edit_prescription/<int:id>/", views.add_prescription, name="edit_prescription"),
    path("edit_feedback/<int:id>/", views.add_feedback, name="edit_feedback"),
]
