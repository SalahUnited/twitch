from flask import Flask
import os
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "Alive"

def run():
    # Получаем порт из переменной окружения, если она задана
    port = int(os.environ.get('PORT', 8080))  # По умолчанию будет использоваться 8080
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)

def keep_alive():  
    t = Thread(target=run)
    t.start()
