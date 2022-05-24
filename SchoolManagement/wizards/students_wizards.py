from odoo import models, fields, api, _


class StudentsWizard(models.TransientModel):
    _name = 'students.wizards'
    _description = 'wizard for student update'

    student_name = fields.Char('Student Name')
    roll_no = fields.Integer('Roll No')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], default='male')

    @api.model
    def default_get(self, fields):
        res = super(StudentsWizard, self).default_get(fields)
        active_model = self.env.context.get('active_id')
        student_id = self.env['students.details'].search([('id', '=', active_model)])
        res.update({
            'student_name': student_id.student_name,
            'roll_no': student_id.roll_no,
            'age': student_id.age,
            'gender': student_id.gender
        })
        return res

    def change_name(self):
        active_model = self.env.context.get('active_id')
        students_id = self.env['students.details'].search([('id', '=', active_model)])
        students_id.update({
            'student_name': self.student_name,
            'roll_no': self.roll_no,
            'age': self.age,
            'gender': self.gender
        })
