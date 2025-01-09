from odoo import http
from odoo.http import request

class CameraDataController(http.Controller):

    @http.route('/api/camera_data', type='json', auth='public', methods=['POST'], csrf=False)
    def receive_camera_data(self, **kwargs):
        data = request.jsonrequest

        # الحقول المطلوبة
        required_fields = ['timestamp', 'camera_id', 'person_id', 'confidence', 'x', 'y', 'width', 'height']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return {'status': 'error', 'message': f'الحقول الناقصة: {", ".join(missing_fields)}'}

        # إنشاء سجل جديد
        record = request.env['camera.data'].sudo().create({
            'timestamp': data['timestamp'],
            'camera_id': data['camera_id'],
            'person_id': data['person_id'],
            'confidence': data['confidence'],
            'x': data['x'],
            'y': data['y'],
            'width': data['width'],
            'height': data['height'],
        })

        return {'status': 'success', 'message': 'تم إدخال البيانات بنجاح', 'record_id': record.id}
