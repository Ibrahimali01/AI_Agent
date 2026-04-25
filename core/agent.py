import os
import sys
import re

# التأكد من رؤية ملف المحرك omni_agent.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from omni_agent import OmniAgent

class AIAgent:
    def __init__(self):
        self.engine = OmniAgent()
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def run_task(self, prompt):
        # تزويد المحرك بقائمة الملفات الحالية عشان يعرف يشتغل عليها
        files = [f for f in os.listdir(self.root_dir) if os.path.isfile(os.path.join(self.root_dir, f))]
        
        enhanced_prompt = f"""
        سياق المشروع: أنت تعمل داخل مجلد يحتوي على الملفات: {files}
        المهمة: {prompt}
        إذا طلبت منك تعديل ملف، استخدم كود بايثون لقراءة الملف وتعديله.
        """
        
        print(f"[*] العميل الشامل يحلل المشروع...")
        # استخدام الدالة اللي أنت قلت إنها شغالة تمام
        response = self.engine.ask_and_execute(enhanced_prompt)
        print(f"\n[AI]: {response}")

if __name__ == "__main__":
    agent = AIAgent()
    # تجربة فحص ذاتي
    agent.run_task("تأكد من أن ملف main.py شغال بشكل صحيح")

