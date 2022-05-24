from odoo import fields, api, models, _
from dateutil.relativedelta import relativedelta
from datetime import date


class StudentsDetails(models.Model):
    _name = 'students.details'
    _description = 'Details of all the students'

    name = fields.Char(string='Reference', required=True, readonly=True, default=lambda self: _('New'))
    student_name = fields.Char('Student Name')
    roll_no = fields.Integer('Roll No')
    age = fields.Integer('Age',compute='_cal_age',store=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], default='male')
    dob = fields.Date('Date of Birth')

    # Many2one fields
    teacher_id = fields.Many2one('teachers.details','Teacher Name')
    school_id = fields.Many2one('different.college','School Name')

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('students.details') or _('New')
        return super(StudentsDetails, self).create(vals)

    @api.depends('dob')
    def _cal_age(self):
        for i in self:
            today = date.today()
            i.age = relativedelta(today, i.dob).years
