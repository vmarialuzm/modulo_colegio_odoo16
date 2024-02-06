from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char('Name', required=True)
    credits = fields.Integer('Credits')
    max_students = fields.Integer('Max Students')
    active = fields.Boolean('Active', default=True)
    student_ids = fields.Many2many('school.student', string='Enrolled Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
