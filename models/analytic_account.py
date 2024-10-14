from odoo import models, fields, api

class AnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    is_blocked = fields.Boolean(string="Blocked", default=False, help="If blocked, this analytic account cannot be used.")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # Filtramos para que las cuentas bloqueadas no aparezcan en algunas vistas
        context = self.env.context
        if context.get('hide_blocked', False):
            args += [('is_blocked', '=', False)]
        return super(AnalyticAccount, self).search(args, offset=offset, limit=limit, order=order, count=count)

    @api.constrains('is_blocked')
    def _check_blocked(self):
        if self.is_blocked:
            # Lógica adicional en caso de necesitar notificaciones al bloquear
            pass
