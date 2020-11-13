from odoo import models, fields


class Course(models.Model):
    _name = "openacademy.course"
    _description = "Courses at the OpenAcademy"

    name = fields.Char(string="Course name", required=True)
    session_ids = fields.One2many(
        comodel_name="openacademy.session", inverse_name="course_id", string="Sessions")

    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], default='beginner')
