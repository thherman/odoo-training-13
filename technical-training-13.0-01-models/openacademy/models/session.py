from odoo import models, fields


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session of a course"

    name = fields.Char(string="Session name")
    course_id = fields.Many2one("openacademy.course", required=True)
    maester_id = fields.Many2one(
        string="Maester", comodel_name="res.partner", required=True)
