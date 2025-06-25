from odoo import http
from odoo.http import Response

class CustomLoginBlocker(http.Controller):

    @http.route('/web/login', type='http', auth='public', website=True, sitemap=False)
    def web_login(self, **kwargs):
        return Response(
            "403 Forbidden: Access to login is blocked.",
            status=403,
            headers={'Content-Type': 'text/plain'}
        )
