from django.contrib import admin
from .models import Patients, PatientGroups, PatientMedicalHistory, \
    PatientVitalSigns, PatientClinicNotes, PatientTreatmentPlans, State, City, Country, \
    PatientFile, PatientPrescriptions, PatientInvoices, PatientPayment, \
    PatientMembership, ProcedureCatalogInvoice


@admin.register(PatientGroups)
class PatientGroupsAdmin(admin.ModelAdmin):
    model = PatientGroups


@admin.register(PatientMedicalHistory)
class PatientMedicalHistoryAdmin(admin.ModelAdmin):
    model = PatientMedicalHistory


@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    model = Patients


@admin.register(PatientVitalSigns)
class PatientVitalSignsAdmin(admin.ModelAdmin):
    model = PatientVitalSigns


@admin.register(PatientClinicNotes)
class PatientClinicNotesAdmin(admin.ModelAdmin):
    model = PatientClinicNotes


@admin.register(PatientTreatmentPlans)
class PatientTreatmentPlansAdmin(admin.ModelAdmin):
    model = PatientTreatmentPlans


@admin.register(PatientFile)
class PatientFileAdmin(admin.ModelAdmin):
    model = PatientFile


@admin.register(PatientPrescriptions)
class PatientPrescriptionsAdmin(admin.ModelAdmin):
    model = PatientPrescriptions


@admin.register(PatientInvoices)
class PatientInvoicesAdmin(admin.ModelAdmin):
    model = PatientInvoices


@admin.register(PatientPayment)
class PatientPaymentAdmin(admin.ModelAdmin):
    model = PatientPayment


@admin.register(PatientMembership)
class PatientMemberShipAdmin(admin.ModelAdmin):
    model = PatientMembership


@admin.register(ProcedureCatalogInvoice)
class ProcedureCatalogInvoiceAdmin(admin.ModelAdmin):
    model = ProcedureCatalogInvoice


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    model = State

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country