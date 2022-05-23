from odoo import fields,api,models, _

class TeachersDetails(models.Model):
    _name = 'teachers.details'
    _description = 'details of all the teachers'

    name = fields.Char(string='Reference',required=True, readonly=True, default= lambda self: _('New'))
    teacher_name = fields.Char('Teacher Name')
    qualification = fields.Char('Qualification')
    subject = fields.Selection(selection=[('eng','English'),('hindi','Hindi'),('mar','Marathi')], default='eng')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], default='male')
    phone = fields.Char('Phone No',size=10)
    no_of_student = fields.Integer('No of Students', compute='no_of_students')
    student_ids = fields.One2many('teachers.details.line', 'student_id', 'Student ids')


    def no_of_students(self):
        no_of_students = self.env['students.details'].search_count([('teacher_id', '=', self.id)])
        print('no of student', no_of_students)
        self.no_of_student = no_of_students

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('teachers.details') or _('New')
        return super(TeachersDetails, self).create(vals)




    def create_student(self):
        student_id = self.env['students.details'].create({
            'student_name':'Aditya',
            'age': 21,
            'gender':'male',
            'teacher_id': self.id
        })

    def write(self, vals):
        res = super(TeachersDetails, self).write(vals)
        for rec in self:
            if rec.qualification == False:
                rec.qualification = 'Teacher'
        return res


class TeacherDetailsLine(models.Model):
    _name = 'teachers.details.line'

    student_name = fields.Many2one('students.details', 'Students Name')
    age = fields.Char(string='Age')

    student_id= fields.Many2one('teachers.details','teacher id')

    # @api.onchange('student_name')
    # def student_onchange(self):
    #     student_name_search = self.env['students.details'].search('id','=',self.student_name.id)
    #     print(student_name_search)



