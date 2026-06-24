#!/data/data/com.termux/files/usr/bin/bash

mkdir -p api/models
mkdir -p api/routes
mkdir -p api/services

mkdir -p database
mkdir -p logs
mkdir -p backups
mkdir -p uploads

mkdir -p static/css
mkdir -p static/js
mkdir -p static/img

mkdir -p templates
mkdir -p node-agent
mkdir -p scripts

cat > requirements.txt << 'EOF'
flask
flask-login
flask-limiter
flask-wtf
sqlalchemy
gunicorn
EOF

cat > README.md << 'EOF'
# Chrono Sovereign Cloud

Infraestructura soberana desarrollada por Chrono Shield Systems.

Características:

- Dashboard web
- Gestión de nodos
- Base SQLite
- Arquitectura Offline First
- Monitoreo de infraestructura
- Hosting soberano
- Preparado para expansión Mesh

EOF

cat > api/config.py << 'EOF'
SECRET_KEY="chrono-shield-2026"
DATABASE="database/chrono.db"
EOF

cat > database/init.sql << 'EOF'
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
);

CREATE TABLE IF NOT EXISTS nodes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
ip TEXT,
status TEXT,
last_seen TEXT
);
EOF

echo "Bootstrap completado"
