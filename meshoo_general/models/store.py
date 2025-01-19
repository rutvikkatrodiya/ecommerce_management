# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StoreStore(models.Model):
    _name = 'store.store'
    _description = 'Stores'
    _order = 'id desc'

    name = fields.Char('Name')
    company_id = fields.Many2one('res.company', string='Company')

    def create_company_for_store(self):
        for rec in self:
            if rec.name and not rec.company_id:
                company_data = {
                    'name': rec.name,
                    'currency_id': self.env.ref('base.INR').id,
                    'parent_id': self.env.ref('meshoo_general.company_meshoo').id,
                }
                company_id = self.env['res.company'].sudo().create(company_data)
                rec.company_id = company_id
