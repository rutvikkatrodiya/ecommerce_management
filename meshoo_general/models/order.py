# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class OrderOrder(models.Model):
    _name = 'order.order'
    _description = 'Orders'
    _rec_name = 'order_number'
    _order = 'id desc'

    order_number = fields.Char('Order Number')
    order_date = fields.Date('Order Date')
    store_id = fields.Many2one('store.store', string='Store')
    company_id = fields.Many2one('res.company', string='Company')
    status = fields.Selection([
        ('draft', 'Draft'), ('pick_up', 'Pick up'), 
        ('return', 'Return'), ('done', 'Done'), ('cancel', 'Cancel'), 
    ], string='Status', default='draft')
    courier = fields.Selection([
        ('valmo', 'Valmo'), ('xpressbees', 'Xpress bees'), 
        ('shadowfax', 'Shadowfax'), ('delhivery', 'Delhivery'), ('ecom', 'Ecom'), 
    ], string='Courier')

    return_type = fields.Selection([
        ('rto', 'Courier Return (RTO)'), ('customer_return', 'Customer Return'), 
    ], string='Return Type')
    return_date = fields.Date('Return Date')
    awb_number = fields.Char('AWB Number')
    product_qty = fields.Integer('Product Qty')
    product_sku = fields.Char('SKU')
    product_size = fields.Char('Size')
    payment_amount = fields.Float('Payment Amount')
    payment_date = fields.Date('Payment Date')

    def action_state_draft(self):
        for rec in self:
            rec.status = 'draft'

    def action_state_pick_up(self):
        for rec in self:
            rec.status = 'pick_up'

    def action_state_return(self):
        for rec in self:
            rec.status = 'return'

    def action_state_done(self):
        for rec in self:
            rec.status = 'done'

    def action_state_cancel(self):
        for rec in self:
            rec.status = 'cancel'
