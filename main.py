"""
Chrono Sovereign Cloud - Dashboard Principal
Sistema de Monitoreo Soberano
Chrono Shield Systems - 2026
"""

from flask import Flask, render_template, jsonify
import os
import platform
import datetime

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/status')
def status():
    """API para estado del sistema"""
    return jsonify({
        "status": "online",
        "version": "0.1.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "system": platform.system(),
        "node": platform.node(),
        "message": "Chrono Sovereign Cloud - Operando en modo soberano"
    })

if __name__ == '__main__':
    print("🚀 Iniciando Chrono Sovereign Cloud - Modo Empresarial")
    print("🌐 Accede al dashboard en: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
