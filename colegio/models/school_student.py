from datetime import date
from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char('Name', required=True)
    birth_date = fields.Date('Birth Date')
    age = fields.Integer("Age", compute='_compute_age', store=True)  # Campo calculado
    final_exam_grade = fields.Float('Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0  # O puedes elegir no establecer nada si no hay fecha de nacimiento
