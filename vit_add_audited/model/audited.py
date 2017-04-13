from openerp import api, fields, models

class res_partner(models.Model):
	_inherit = "res.partner"

	audited = fields.Boolean(string='Audited')