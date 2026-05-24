# from odoo import models, fields, api


# class account-module3(models.Model):
#     _name = 'account-module3.account-module3'
#     _description = 'account-module3.account-module3'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

