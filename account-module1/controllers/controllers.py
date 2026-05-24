# from odoo import http


# class Account-module1(http.Controller):
#     @http.route('/account-module1/account-module1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account-module1/account-module1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account-module1.listing', {
#             'root': '/account-module1/account-module1',
#             'objects': http.request.env['account-module1.account-module1'].search([]),
#         })

#     @http.route('/account-module1/account-module1/objects/<model("account-module1.account-module1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account-module1.object', {
#             'object': obj
#         })

