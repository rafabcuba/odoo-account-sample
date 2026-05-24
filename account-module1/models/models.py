# from odoo import models, fields, api


# class account-module1(models.Model):
#     _name = 'account-module1.account-module1'
#     _description = 'account-module1.account-module1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

