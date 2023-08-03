from base.models import TimeStampedModel
from inventory.models import InventoryItem
from patients.models import Patients, PatientPrescriptions, Reservations
from practice.models import Practice, PracticeStaff, ProcedureCatalog, Taxes, PracticeOffers, DrugUnit, DrugType
from django.db import models


class ProcedureCatalogProforma(TimeStampedModel):
    procedure = models.ForeignKey(ProcedureCatalog, blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=256, null=True, blank=True)
    unit_cost = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    offers = models.ForeignKey(PracticeOffers, blank=True, null=True, on_delete=models.PROTECT)
    unit = models.PositiveSmallIntegerField(blank=True, null=True)
    default_notes = models.TextField(null=True, blank=True)
    taxes = models.ManyToManyField(Taxes, blank=True)
    is_active = models.BooleanField(default=True)
    doctor = models.ForeignKey(PracticeStaff, blank=True, null=True, on_delete=models.PROTECT)
    date = models.DateField(blank=True, null=True)
    total = models.FloatField(null=True, blank=True)
    tax_value = models.FloatField(null=True, blank=True)
    discount_value = models.FloatField(null=True, blank=True)


class InventoryCatalogProforma(TimeStampedModel):
    inventory = models.ForeignKey(InventoryItem, blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=1024, blank=True, null=True)
    drug_unit = models.ForeignKey(DrugUnit, blank=True, null=True, on_delete=models.PROTECT)
    drug_type = models.ForeignKey(DrugType, blank=True, null=True, on_delete=models.PROTECT)
    strength = models.IntegerField(blank=True, null=True)
    dosage = models.CharField(max_length=1024, blank=True, null=True)
    frequency = models.CharField(max_length=1024, blank=True, null=True)
    unit = models.PositiveSmallIntegerField(blank=True, null=True)
    unit_cost = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    offers = models.ForeignKey(PracticeOffers, blank=True, null=True, on_delete=models.PROTECT)
    taxes = models.ManyToManyField(Taxes, blank=True)
    doctor = models.ForeignKey(PracticeStaff, blank=True, null=True, on_delete=models.PROTECT)
    instruction = models.CharField(max_length=1024, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    total = models.FloatField(null=True, blank=True)
    tax_value = models.FloatField(null=True, blank=True)
    discount_value = models.FloatField(null=True, blank=True)
    batch_number = models.CharField(max_length=1024, blank=True, null=True)
    date = models.DateField(blank=True, null=True)


class PatientProformaInvoices(TimeStampedModel):
    practice = models.ForeignKey(Practice, blank=True, null=True, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.PROTECT)
    staff = models.ForeignKey(PracticeStaff, blank=True, null=True, on_delete=models.PROTECT)
    procedure = models.ManyToManyField(ProcedureCatalogProforma, blank=True)
    inventory = models.ManyToManyField(InventoryCatalogProforma, blank=True)
    prescription = models.ManyToManyField(PatientPrescriptions, blank=True)
    cost = models.FloatField(null=True, blank=True, default=0)
    discount = models.FloatField(null=True, blank=True, default=0)
    taxes = models.FloatField(null=True, blank=True, default=0)
    total = models.FloatField(null=True, blank=True, default=0)
    is_pending = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_cancelled = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    invoice_id = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True, default="Invoice")
    notes = models.CharField(max_length=2000, blank=True, null=True)
    promo_code = models.CharField(max_length=512, null=True, blank=True)
    courier_charge = models.FloatField(null=True, blank=True)
    courier_name = models.CharField(max_length=512, null=True, blank=True)
    tracking_number = models.CharField(max_length=512, null=True, blank=True)
    tracking_bill = models.CharField(max_length=512, null=True, blank=True)
    delivery_address = models.CharField(max_length=4000, null=True, blank=True)
    delivery_contact = models.CharField(max_length=100, null=True, blank=True)
    cancel_note = models.CharField(max_length=1000, null=True, blank=True)
