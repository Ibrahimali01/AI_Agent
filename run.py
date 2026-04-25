#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import platform

def main():
    system = platform.system()
    print(f"نظام التشغيل: {system}")
    
    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/home"):
            print("بيئة ترمكس")
            # أوامر خاصة بترمكس
            os.system("clear")
        else:
            print("لينكس عادي")
            # أوامر لينكس العادية
            os.system("clear")
    elif system == "Windows":
        print("ويندوز")
        os.system("cls")
    else:
        print("نظام غير مدعوم")
        sys.exit(1)
    
    # تشغيل البرنامج الرئيسي
    print("تشغيل البرنامج...")
    # هنا يمكن استدعاء ملف رئيسي مثل main.py
    # import main
    # main.start()

if __name__ == "__main__":
    main()
