# mysite
วิธีการใช้งานและติดตั้ง
Download ไฟล์ZIP 
และทำการ extract files ไว้ที่ใดก็ได้
จากนั้นทำการ เปิดโปรแกรม visual studio code หรือ PyCharm
ไปที่ File > OPEN > เลือก Folder ที่ทำการ extract files ไว้ กด OK
ไปที่ Terminal พิมพ์คำสั่ง python manage.py runserver

จำเป็นต้องมี Python 3+ , Django
วิธีติดตั้ง 
ติดตั้ง Python 
- สำหรับ Windows สามารถ Download ได้จาก https://www.python.org/downloads/ เลือก Download Python
สำคัญมากต้องติ๊กช่อง “Add python 3.X to PATH” ด้วย
- สำหรับ Linux version ใหม่ๆ จะมี python3 ติดตั้งมาให้ โดย default อยู่แล้ว
- สำหรับ Mac สามารถทำตาม Tutorial นี้ เพื่อติดตั้งได้
https://docs.python-guide.org/starting/install3/osx/

ติดตั้ง Django
เปิด command prompt
พิมพ์คำสั่ง $ pip install -U Django 
แล้ว pip3 จะ download django เข้ามาติดตั้งในเครื่องให้โดยอัตโนมัติ

พิมพ์คำสั่ง
python manage.py migrat
และ
พิมพ์คำสั่ง
สร้างSuperuser ไว้ใช้งาน ฐานข้อมูล
python manage.py createsuperuser


อ้างอิง
https://codeburst.io/%E0%B9%80%E0%B8%A3%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2-web-application-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2-python-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-django-framework-38ce132ac706

https://tutorial.djangogirls.org/en/django_admin/
