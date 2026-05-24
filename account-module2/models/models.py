# from odoo import models, fields, api


# class account-module2(models.Model):
#     _name = 'account-module2.account-module2'
#     _description = 'account-module2.account-module2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

