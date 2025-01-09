
# Camera Data Receiver API

### وصف المشروع
واجهة برمجية (API) مصممة لتخزين بيانات الكاميرات في قاعدة بيانات Odoo. هذه الواجهة تتيح للأنظمة الأخرى إرسال البيانات وتخزينها بطريقة منظمة.

---

## **واجهة API**

### **1. عنوان API**
http://<HOST>:<PORT>/jsonrpc

markdown
نسخ الكود

#### **إعدادات الاتصال**
- **HOST**: عنوان الخادم (مثال: `localhost`).
- **PORT**: منفذ Odoo (افتراضي: `8069`).
- **DB**: اسم قاعدة البيانات.
- **USER**: اسم المستخدم أو البريد الإلكتروني.
- **PASS**: كلمة المرور.

---

### **2. خطوات استخدام API**

#### **1. تسجيل الدخول**
يتم تسجيل الدخول باستخدام الخدمة `common.login` للحصول على معرّف المستخدم (`uid`).

##### **الطلب**
```json
{
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "common",
        "method": "login",
        "args": ["<DATABASE_NAME>", "<USER_EMAIL>", "<USER_PASSWORD>"]
    },
    "id": 1
}
الرد
json
نسخ الكود
{
    "result": <USER_ID>
}
2. إرسال بيانات الكاميرات
بعد تسجيل الدخول، يتم إرسال بيانات الكاميرات باستخدام الخدمة object.execute.

الطلب
json
نسخ الكود
{
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute",
        "args": [
            "<DATABASE_NAME>",
            <USER_ID>,
            "<USER_PASSWORD>",
            "camera.data",
            "create",
            {
                "timestamp": "2025-01-09 12:34:56",
                "camera_id": "CAM123",
                "person_id": "PERSON456",
                "confidence": 0.95,
                "x": 100.0,
                "y": 200.0,
                "width": 50.0,
                "height": 75.0
            }
        ]
    },
    "id": 2
}
الرد
json
نسخ الكود
{
    "result": <NEW_RECORD_ID>
}
3. الحقول المطلوبة
الحقل	النوع	الوصف	مثال
timestamp	Datetime	التاريخ والوقت	2025-01-09 12:34:56
camera_id	String	معرف الكاميرا	CAM123
person_id	String	معرف الشخص	PERSON456
confidence	Float	مستوى الثقة	0.95
x	Float	الإحداثي X	100.0
y	Float	الإحداثي Y	200.0
width	Float	عرض الكائن	50.0
height	Float	ارتفاع الكائن	75.0
استخدام API في Python
1. تسجيل الدخول
python
نسخ الكود
import json
import random
import urllib.request

url = "http://localhost:8069/jsonrpc"
db = "your_database_name"
user = "admin"
password = "admin"

data = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "common",
        "method": "login",
        "args": [db, user, password]
    },
    "id": random.randint(0, 1000000000),
}

req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
    "Content-Type": "application/json",
})
response = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
uid = response["result"]
print(f"Logged in as UID: {uid}")
2. إرسال بيانات الكاميرات
python
نسخ الكود
camera_data = {
    "timestamp": "2025-01-09 12:34:56",
    "camera_id": "CAM123",
    "person_id": "PERSON456",
    "confidence": 0.95,
    "x": 100.0,
    "y": 200.0,
    "width": 50.0,
    "height": 75.0
}

data = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute",
        "args": [db, uid, password, "camera.data", "create", camera_data]
    },
    "id": random.randint(0, 1000000000),
}

req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
    "Content-Type": "application/json",
})
response = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
record_id = response["result"]
print(f"Record created with ID: {record_id}")
استكشاف الأخطاء وإصلاحها
المشكلة: فشل تسجيل الدخول. الحل: تحقق من اسم قاعدة البيانات، البريد الإلكتروني، وكلمة المرور.

المشكلة: فشل إنشاء السجل. الحل: تأكد من إرسال جميع الحقول المطلوبة.

نصائح
استخدم Postman لاختبار الطلبات بسهولة.
تحقق من سجلات Odoo (odoo.log) عند مواجهة أي مشكلة.
حقوق الملكية
تم تطوير هذا المشروع لدعم التكامل بين الأنظمة وOdoo.

yaml
نسخ الكود

---
