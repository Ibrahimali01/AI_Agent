#!/bin/bash
echo "python3 $(pwd)/omni_agent.py" > agent
chmod +x agent
mv agent ../usr/bin/
echo "[+] الآن يمكنك كتابة 'agent' في أي مكان للبدء."

