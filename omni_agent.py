from dotenv import load_dotenv
import json
import os
import requests

# إعداد البيئة
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
        self.available_models = []
        self.current_model = None

    def auto_discover_models(self):
        """يسحب كل الموديلات المتاحة ويصفي المجاني منها فقط"""
        try:
            res = requests.get(f"{self.base_url}/models", headers=self.headers)
            data = res.json().get('data', [])
            # جلب كل ما هو مجاني (free) من القائمة الحية
            self.available_models = [m['id'] for m in data if 'free' in m['id']]
            
            if not self.available_models:
                # إذا لم يجد مجاني، يأخذ أول 10 موديلات من القائمة العامة كبديل
                self.available_models = [m['id'] for m in data[:10]]

            self.current_model = self.available_models[0]
            print(f"[+] تم العثور على {len(self.available_models)} موديل متاح للتبديل.")
        except Exception as e:
            print(f"[!] فشل سحب قائمة الموديلات: {e}")

    def switch_model(self):
        """يحذف الموديل الحالي المعطل وينتقل للي بعده فوراً"""
        if self.current_model in self.available_models:
            self.available_models.remove(self.current_model)
        
        if self.available_models:
            self.current_model = self.available_models[0]
            print(f"[!] تم التبديل اللحظي إلى الموديل التالي: {self.current_model}")
            return True
        else:
            print("[!!!] تم استنفاد كافة النماذج المتاحة.")
            return False

    def ask_and_execute(self, prompt):
        """محاولة التنفيذ عبر التبديل التلقائي اللحظي"""
        while self.available_models:
            print(f"[*] محاولة التنفيذ باستخدام {self.current_model}...")

            payload = {
                "model": self.current_model,
                "messages": [
                    {"role": "system", "content": "You are a Termux AI. Output ONLY raw Python code. No text."},
                    {"role": "user", "content": prompt}
                ]
            }

            try:
                res = requests.post(f"{self.base_url}/chat/completions", headers=self.headers, json=payload, timeout=20)
                res_data = res.json()

                if 'choices' in res_data:
                    code = res_data['choices'][0]['message']['content']
                    code = code.replace("```python", "").replace("```", "").strip()
                    
                    print("\n" + "="*30 + f"\n[+] الكود من {self.current_model}:\n" + "="*30)
                    print(code)
                    
                    print("[*] جاري التنفيذ...")
                    exec(code, globals())
                    print("[+] تم تنفيذ المهمة بنجاح.")
                    break 

                else:
                    print(f"[-] الموديل {self.current_model} رفض الطلب أو وصل للحد الأقصى.")
                    if not self.switch_model(): break

            except Exception as e:
                print(f"[!] خطأ في {self.current_model}: {e}")
                if not self.switch_model(): break

def main():
    agent = OmniAgent()
    agent.auto_discover_models()

    print("\n" + "★"*40)
    print("🤖 OMNI-AGENT: DYNAMIC SWITCH MODE")
    print("نظام التبديل التلقائي بين كافة الموديلات نشط")
    print("★"*40)

    while True:
        task = input("\nماذا تريدني أن أفعل؟ (أو اكتب 'خروج'): ")
        if task.lower() in ['خروج', 'exit']: break
        if task.strip(): agent.ask_and_execute(task)

if __name__ == "__main__":
    main()

