# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PaymentImport(models.Model):
    _name = 'payment.import'
    _description = 'Payment Import'
    _order = 'id desc'

    payment_file = fields.Binary('Payment File')
    payment_file_name = fields.Char('Payment File Name')
    store_id = fields.Many2one('store.store')
    status = fields.Selection([
        ('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel'),
    ], string='Status', default='draft')

    def action_process_payment_file(self):
        for rec in self:
            if rec.payment_file and rec.store_id:
                pass
