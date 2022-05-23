from odoo import fields,api,models, _




class DifferentCollege(models.Model):
    _name = 'different.college'
    _rec_name = 'college_name'
    _description = 'here we will have different school'

    college_name = fields.Char('College Name')
    location = fields.Char('Location')
    stream = fields.Selection(selection=[('science','Science'),('commerce','Commerce'),('arts','Arts')], default='science')
