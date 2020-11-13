from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session of a course"

    @api.model
    def default_get(self, default_fields):
        values = super().default_get(default_fields)
        if 'course_id' in default_fields and values.get('course_id'):
            parent = self.browse(values.get('course_id'))
            values['course_id'] = parent.id
        return values

    course_id = fields.Many2one(
        string="Course", comodel_name="openacademy.course", required=True)

    maester_id = fields.Many2one(
        string="Maester", comodel_name="res.partner", required=True)

    name = fields.Char(string="Session name", required=True)
    course_name = fields.Char(string="Course name", related="course_id.name")

    
