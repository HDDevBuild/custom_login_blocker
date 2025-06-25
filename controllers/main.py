from odoo import http
from odoo.http import Response

class BlockWebLogin(http.Controller):

    @http.route('/web/login', type='http', auth='public', website=True, sitemap=False)
    def block_login(self, **kwargs):
        return Response(
            """
            <html>
                <head><title>Access Denied</title></head>
                <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
                    <h1 style="color: #d9534f;">403 - Access Denied</h1>
                    <p style="font-size: 18px;">
                        You are not allowed to access this page.
                    </p>
                    <p style="font-size: 16px;">
                        Please contact the administrator if you believe this is a mistake.
                    </p>
                </body>
            </html>
            """,
            status=403,
            headers={'Content-Type': 'text/html'}
        )

    @http.route('/web', type='http', auth='public', website=True, sitemap=False)
    def block_web(self, **kwargs):
        return Response(
            """
            <html>
                <head><title>Access Denied</title></head>
                <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
                    <h1 style="color: #d9534f;">403 - Access Denied</h1>
                    <p style="font-size: 18px;">
                        Access to this page is restricted.
                    </p>
                    <p style="font-size: 16px;">
                        If you need help, please contact the system administrator.
                    </p>
                </body>
            </html>
            """,
            status=403,
            headers={'Content-Type': 'text/html'}
        )
