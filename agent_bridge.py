import os
import sys

# إضافة المسار الحالي للمسار البرمجي
sys.path.append(os.getcwd())

try:
    from omni_agent import OmniAgent
    from tools.system_tool import SystemTool
    print("✅ تم استدعاء العقل والأدوات بنجاح!")
except ImportError as e:
    print(f"❌ خطأ: تأكد من وجود ملف omni_agent.py ومجلد tools: {e}")
    sys.exit(1)

class AgentBridge:
    def __init__(self):
        self.ai = OmniAgent()
        self.system = SystemTool()
        print("[*] الجسر (alAgent Bridge) شغال دلوقتي..")

    def run_check(self):
        info = self.system.get_system_info()
        print(f"[+] شغال على نظام: {info['platform']}")
        print("[+] مبروك.. الجسر ربط كل حاجة ببعضها!")

if __name__ == "__main__":
    bridge = AgentBridge()
    bridge.run_check()
