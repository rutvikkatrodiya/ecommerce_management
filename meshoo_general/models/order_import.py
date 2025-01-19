# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class OrderImport(models.Model):
    _name = 'order.import'
    _description = 'Order Import'
    _order = 'id desc'

    order_file = fields.Binary('Order File')
    order_file_name = fields.Char('Order File Name')
    store_id = fields.Many2one('store.store')
    status = fields.Selection([
        ('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancel'),
    ], string='Status', default='draft')

    def action_process_order_file(self):
        for rec in self:
            if rec.order_file and rec.store_id:
                pass
