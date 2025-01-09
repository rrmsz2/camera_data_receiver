import json
import random
import urllib.request

# إعدادات الاتصال بـ Odoo
HOST = 'localhost'
PORT = 8050
DB = 'raidtest'  # اسم قاعدة البيانات
USER = 'rrmsz2@gmail.com'  # اسم المستخدم
PASS = 'b88e53b090f730d5af42c1c1268c708b4c2c681c'  # كلمة المرور

# دالة لإرسال طلب JSON-RPC
def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type": "application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

# دالة للاتصال بالخدمات المختلفة
def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# تسجيل الدخول إلى قاعدة البيانات
url = f"http://{HOST}:{PORT}/jsonrpc"
uid = call(url, "common", "login", DB, USER, PASS)

# إنشاء سجل جديد في نموذج بيانات الكاميرات
args = {
    'timestamp': '2025-01-09 12:34:56',
    'camera_id': 'CAM123',
    'person_id': 'PERSON456',
    'confidence': 0.95,
    'x': 100.0,
    'y': 200.0,
    'width': 50.0,
    'height': 75.0,
}
record_id = call(url, "object", "execute", DB, uid, PASS, 'camera.data', 'create', args)

print(f"Record Created with ID: {record_id}")
