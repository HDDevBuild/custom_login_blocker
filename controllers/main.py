from odoo import http
from odoo.http import Response

# class CustomLoginBlocker(http.Controller):

#     @http.route('/web/login', type='http', auth='public', website=True, sitemap=False)
#     def web_login(self, **kwargs):
#         message = """
#         <html>
#             <head><title>Access Denied</title></head>
#             <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
#                 <h1 style="color: #d9534f;">500 - Access Denied</h1>
#                 <p style="font-size: 18px;">
#                     You do not have permission to access the login page at this time.
#                 </p>
#                 <p style="font-size: 16px;">
#                     If you believe this is a mistake, please contact the system administrator or support team.
#                 </p>
#             </body>
#         </html>
#         """
#         return Response(
#             message,
#             status=500,
#             headers={'Content-Type': 'text/html'}
#        )


from odoo import http

class CrashLogin(http.Controller):

    @http.route('/web/login', type='http', auth='public', website=True, sitemap=False)
    def crash_login(self, **kwargs):
        raise Exception("💥 Intentional Crash: Simulating Internal Server Error")