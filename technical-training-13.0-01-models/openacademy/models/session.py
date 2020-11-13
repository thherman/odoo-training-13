from odoo import models, fields


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session of a course"

    course_id = fields.Many2one(
        string="Course", comodel_name="openacademy.course", required=True)

    maester_id = fields.Many2one(
        string="Maester", comodel_name="res.partner", required=True)

    name = fields.Char(string="Session name", required=True)
    course_name = fields.Char(string="Course name", related="course_id.name")
