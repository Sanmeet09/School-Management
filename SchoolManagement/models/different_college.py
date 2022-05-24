from odoo import fields, api, models, _


class DifferentCollege(models.Model):
    _name = 'different.college'
    _rec_name = 'college_name'
    _description = 'here we will have different school'

    name = fields.Char(string='Reference', required=True, readonly=True, default=lambda self: _('New'))
    college_name = fields.Char('College Name')
    location = fields.Many2many(comodel_name='product.template', string='Location')
    stream = fields.Selection(selection=[('science', 'Science'), ('commerce', 'Commerce'), ('arts', 'Arts')],
                              default='science')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('different.college') or _('New')
        return super(DifferentCollege, self).create(vals)
