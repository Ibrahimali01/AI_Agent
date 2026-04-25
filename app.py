import eventlet

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import os, time, subprocess

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def get_sys_info():
    try:
        # قراءة استهلاك الرام من نظام أندرويد/ترمكس مباشرة
        mem = subprocess.check_output("free -m", shell=True).decode().split('\n')[1].split()
        total, used, free = int(mem[1]), int(mem[2]), int(mem[3])
        # قراءة الـ Load Average
        with open("/proc/loadavg", "r") as f:
            load = f.read().split()
        return {
            "mem_total": total, "mem_used": used, "mem_free": free,
            "mem_percent": round((used/total)*100, 1),
            "load_1": load[0], "load_5": load[1], "load_15": load[2]
        }
    except:
        return {"error": "Could not read system data"}

@app.route('/')
def index():
    return render_template('index.html')

def background_thread():
    while True:
        data = get_sys_info()
        socketio.emit('sys_update', data)
        socketio.sleep(2)

@socketio.on('connect')
def connect():
    print("Client connected")
    socketio.start_background_task(background_thread)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
