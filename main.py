from core.agent import AIAgent

def main():
    agent = AIAgent()
    print("🤖 العميل الذكي جاهز للعمل على Termux!")
    while True:
        cmd = input("\nاكتب ما تريد تنفيذه (أو خروج): ")
        if cmd == "خروج": break
        agent.run_task(cmd)

if __name__ == "__main__":
    main()
