from odoo import fields, api, models, _


class TeacherWizard(models.TransientModel):
    _name = 'teachers.wizard'

    teacher_name = fields.Char('Teacher Name')
    qualification = fields.Char('Qualification')
    age = fields.Integer('Age')
    phone = fields.Char('Phone No', size=10)

    def create_teacher(self):
        teacher_id = self.env['teachers.details'].create({
            'teacher_name': self.teacher_name,
            'qualification': self.qualification,
            'age': self.age,
            'phone': self.phone
        })
