# from odoo import http


# class Account-module3(http.Controller):
#     @http.route('/account-module3/account-module3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account-module3/account-module3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account-module3.listing', {
#             'root': '/account-module3/account-module3',
#             'objects': http.request.env['account-module3.account-module3'].search([]),
#         })

#     @http.route('/account-module3/account-module3/objects/<model("account-module3.account-module3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account-module3.object', {
#             'object': obj
#         })

