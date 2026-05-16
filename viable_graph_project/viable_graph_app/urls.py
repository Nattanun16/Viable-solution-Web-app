from django.urls import path
from . import views  # ดึงฟังก์ชันมาจาก views.py ที่เราเพิ่งแก้ตะกี้

urlpatterns = [
    # ผูกลิงก์หน้าแรกสุด ('' คือไม่มีอะไรต่อท้าย) ให้วิ่งไปเรียกฟังก์ชัน home
    path('', views.home, name='home'), 
]