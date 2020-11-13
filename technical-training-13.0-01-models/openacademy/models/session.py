from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session of a course"

    @api.model
    def _default_course_id(self):
        _logger.info(self.env.context)
        if self.env.context.get("openacademy.course"):
            return self.env.context.get("openacademy.course")

    _logger.info("YOOOOOOO")
    course_id = fields.Many2one(
        string="Course", comodel_name="openacademy.course", required=True, default=_default_course_id)

    maester_id = fields.Many2one(
        string="Maester", comodel_name="res.partner", required=True)

    name = fields.Char(string="Session name", required=True)
    course_name = fields.Char(string="Course name", related="course_id.name")

    
