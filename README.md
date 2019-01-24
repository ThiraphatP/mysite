# mysite
วิธีการใช้งานและติดตั้ง

การใช้งาน
Download ไฟล์ZIP 
และทำการ extract files ไว้ที่ใดก็ได้
จากนั้นทำการ เปิดโปรแกรม visual studio code หรือ PyCharm
ไปที่ File > OPEN > เลือก Folder ที่ทำการ extract files ไว้ กด OK

จำเป็นต้องมี Python 3+ , Django , superuser

วิธีติดตั้ง 
1. ติดตั้ง Python 
- สำหรับ Windows สามารถ Download ได้จาก https://www.python.org/downloads/ เลือก Download Python
สำคัญมากต้องติ๊กช่อง “Add python 3.X to PATH” ด้วย
- สำหรับ Linux version ใหม่ๆ จะมี python3 ติดตั้งมาให้ โดย default อยู่แล้ว
- สำหรับ Mac สามารถทำตาม Tutorial นี้ เพื่อติดตั้งได้
https://docs.python-guide.org/starting/install3/osx/

2. ติดตั้ง pip3
pip3 คือ package manager ที่ใช้สำหรับติดตั้ง package เสริมให้กับ Python3 (คล้ายๆ คำสั่ง apt-get บน linux) โดยเราจะใช้ pip ในการติดตั้ง Django ต่อไป
- สำหรับ Windows คำสั่ง pip จะถูกติดตั้งมาอยู่แล้วบน python version 3.5 ขึ้นไป 
- สำหรับ Linux ติดตั้งด้วยคำสั่ง $ sudo apt-get install python3-pip
- สำหรับ Mac ทำตาม Link ด้านบนเพื่อติดตั้ง pip3
เมื่อติดตั้งเสร็จสิ้นทดสอบด้วยการพิมพ์คำสั่ง $ pip3 ใน console

3. ติดตั้ง Django
เปิด command prompt
พิมพ์คำสั่ง $ pip install -U Django 
แล้ว pip3 จะ download django เข้ามาติดตั้งในเครื่องให้โดยอัตโนมัติ

4. ไปที่ root directory ของไฟล์
ไปที่ Terminal พิมพ์คำสั่ง
python manage.py migrate


5. สร้าง Superuser เพื่อใช้งาน ฐานข้อมูล sqlite ด้วยคำสั่ง 
python manage.py createsuperuser
จากนั้นไปที่ http://127.0.0.1:8000/admin เพื่อ Login เข้าใช้งาน ฐานข้อมูล

6. เปิดโปรแกรม visual studio code หรือ PyCharm เปิดโฟล์เดอร์ที่เก็บไฟล์
ไปที่ Terminal พิมพ์คำสั่ง python manage.py runserver เพื่อ ทดสอบการทำงาน

*จำเป็นต้องทำทุกขั้นตอน เพื่อป้องกันการ ERROR 
*ต้องเพิ่มข้อมูลก่อน ฟังชั่น Pop ถึงจะทำงาน
*ต้อง Login admin ก่อนจึงจะสามารถใช้ฟังชั่น Push เพื่อเก็บข้อมูลได้

ตัวอย่าง
https://www.picz.in.th/image/50519873-2138234319569534-8942117950312153088-n.TYHmYz

อ้างอิง
https://codeburst.io/%E0%B9%80%E0%B8%A3%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%9E%E0%B8%B1%E0%B8%92%E0%B8%99%E0%B8%B2-web-application-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2-python-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-django-framework-38ce132ac706

https://tutorial.djangogirls.org/en/django_admin/

สอบถามเพิ่มเติม
EMAIL: Thiraphat_p-st@rmutsb.ac.th
