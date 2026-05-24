# from odoo import http


# class Account-module2(http.Controller):
#     @http.route('/account-module2/account-module2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account-module2/account-module2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account-module2.listing', {
#             'root': '/account-module2/account-module2',
#             'objects': http.request.env['account-module2.account-module2'].search([]),
#         })

#     @http.route('/account-module2/account-module2/objects/<model("account-module2.account-module2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account-module2.object', {
#             'object': obj
#         })

