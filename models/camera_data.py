from odoo import models, fields

class CameraData(models.Model):
    _name = 'camera.data'
    _description = 'بيانات الكاميرات'

    timestamp = fields.Datetime(string="التاريخ والوقت", required=True)
    camera_id = fields.Char(string="معرف الكاميرا", required=True)
    person_id = fields.Char(string="معرف الشخص", required=True)
    confidence = fields.Float(string="مستوى الثقة", required=True)
    x = fields.Float(string="الإحداثي X", required=True)
    y = fields.Float(string="الإحداثي Y", required=True)
    width = fields.Float(string="العرض", required=True)
    height = fields.Float(string="الارتفاع", required=True)
