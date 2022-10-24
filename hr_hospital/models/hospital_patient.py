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
