import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    active = fields.Boolean(
        default=True, )

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors'

    doctor_speciality = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    active = fields.Boolean(
        default=True, )

class PatientCard(models.Model):
    _name = 'patient.card'
    _description = 'Patient Card'

    visit_date = fields.Date()
    visit_diagnose = fields.Char()
    visit_prescription = fields.Char()
    active = fields.Boolean(
        default=True, )

class DoctorDiagnose(models.Model):
    _name = 'doctor.diagnose'
    _description = 'Diagnose'

    diagnose_date = fields.Date()
    doctor_diagnose = fields.Char()
    active = fields.Boolean(
        default=True, )
