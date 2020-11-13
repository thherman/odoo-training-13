from odoo import models, fields


class Maester(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    _description = "Maester assigned to a session"

    session_ids = fields.One2many(
        comodel_name="openacademy.session", inverse_name="course_id", string="Sessions")
