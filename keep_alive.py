from flask import Flask
import os
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

def run():
    # Получаем порт из переменной окружения, которая будет настроена Render
    port = int(os.environ.get('PORT', 8080))  # Если переменная PORT не установлена, используем 8080
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)

def keep_alive():  
    t = Thread(target=run)
    t.start()
