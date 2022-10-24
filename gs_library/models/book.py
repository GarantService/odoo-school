import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'gs.lib.book'
    _description = 'Book'

    name = fields.Char(groups='base.group_user')

    active = fields.Boolean(
        default=True,)
    isbn = fields.Char(groups='base.group_user')
