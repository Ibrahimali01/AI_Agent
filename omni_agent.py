from dotenv import load_dotenv
import json
import os
import requests
import time

# 1. إعداد البيئة ومفتاح الـ API
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY") or "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"

class OmniAgent:
    def __init__(self):
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "http://localhost:3000",
            "Content-Type": "application/json"
        }
        self.free_models = []
        self.current_model_index = 0

    def auto_discover_models(self):
        """يجلب قائمة بكل الموديلات المجانية المتاحة حالياً"""
        print("[*] جاري مسح كافة الموديلات المجانية المتاحة...")
        try:
            res = requests.get(f"{self.base_url}/models", headers=self.headers)
            data = res.json().get('data', [])
            # تصفية الموديلات التي تحتوي على كلمة 'free' في اسمها
            self.free_models = [m['id'] for m in data if ':free' in m['id']]
            
            if not self.free_models:
                # إذا لم يجد مجاني، يأخذ أول 5 موديلات عامة كاحتياطي
                self.free_models = [m['id'] for m in data[:5]]
            
            print(f"[+] تم العثور على {len(self.free_models)} موديل متاح للتبديل.")
        except Exception as e:
            print(f"[!] فشل المسح، تأكد من الاتصال: {e}")
            self.free_models = ["google/gemini-2.0-flash-001"] # احتياطي نهائي

    def rotate_model(self):
        """ينتقل للموديل التالي في القائمة"""
        self.current_model_index = (self.current_model_index + 1) % len(self.free_models)
        print(f"[!] تم التبديل إلى الموديل التالي: {self.free_models[self.current_model_index]}")

    def ask_and_execute(self, prompt):
        """يحاول تنفيذ الطلب ويمر عبر الموديلات في حال الفشل"""
        attempts = 0
        max_attempts = len(self.free_models)

        while attempts < max_attempts:
            current_model = self.free_models[self.current_model_index]
            print(f"[*] محاولة التنفيذ باستخدام {current_model}...")

            system_msg = (
                "You are an autonomous AI Agent for Termux. "
                "Your goal is to perform the user task by writing Python code. "
                "Output ONLY the raw python code. No markdown, no explanations. "
                "If the task requires a new skill, write the function for it and call it."
            )

            payload = {
                "model": current_model,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt}
                ]
            }

            try:
                res = requests.post(f"{self.base_url}/chat/completions", headers=self.headers, json=payload)
                res_data = res.json()

                # التحقق من نجاح الرد أو وجود خطأ Rate Limit
                if 'choices' in res_data:
                    code = res_data['choices'][0]['message']['content']
                    code = code.replace("```python", "").replace("```", "").strip()

                    print("\n" + "="*30 + "\n[+] الكود المستلم:\n" + "="*30)
                    print(code)
                    print("="*30 + "\n")

                    print("[*] جاري التنفيذ على النظام...")
                    exec(code, globals())
                    print("[+] تم تنفيذ المهمة بنجاح.")
                    return # الخروج من الدالة بعد النجاح
                
                elif 'error' in res_data and res_data['error'].get('code') == 429:
                    print(f"[-] الموديل {current_model} وصل للحد الأقصى (Rate Limit).")
                    self.rotate_model()
                    attempts += 1
                else:
                    print(f"[-] خطأ غير متوقع من {current_model}: {res_data.get('error')}")
                    self.rotate_model()
                    attempts += 1

            except Exception as e:
                print(f"[!] حدث خطأ مفاجئ أثناء الاتصال بـ {current_model}: {e}")
                self.rotate_model()
                attempts += 1
        
        print("[!!!] فشلت جميع المحاولات مع كافة الموديلات المتاحة.")

def main():
    agent = OmniAgent()
    agent.auto_discover_models()

    print("\n" + "★"*20)
    print("🤖 OMNI-AGENT READY (MULTI-MODEL MODE)")
    print("نظام التبديل التلقائي نشط")
    print("★"*20)

    while True:
        task = input("\nماذا تريدني أن أفعل؟ (أو اكتب 'خروج'): ")
        if task.lower() in ['خروج', 'exit', 'quit']:
            break

        if not task.strip(): continue

        agent.ask_and_execute(task)

if __name__ == "__main__":
    main()

