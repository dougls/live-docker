from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Conectado ao PostgreSQL: {db_version}"
    except Exception as e:
        return f"Erro ao conectar ao banco: {str(e)}"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")