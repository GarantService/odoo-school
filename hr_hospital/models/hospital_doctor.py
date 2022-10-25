from odoo import models, fields


class HospitalDoctor(models.Model):  # Потрібно відокремлювати кожну модель у окремий файл, це значно спростить подальшу роботу з модулем.
    _name = 'hospital.doctor'
    _description = 'Doctors'

    doctor_speciality = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    active = fields.Boolean(
        default=True, )
