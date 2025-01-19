# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ReturnImport(models.Model):
    _name = 'return.import'
    _description = 'Return Import'
    _order = 'id desc'

    return_file = fields.Binary('Return File')
    return_file_name = fields.Char('Return File Name')
    store_id = fields.Many2one('store.store')
    status = fields.Selection([
        ('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel'),
    ], string='Status', default='draft')

    def action_process_payment_file(self):
        for rec in self:
            if rec.return_file and rec.store_id:
                pass
