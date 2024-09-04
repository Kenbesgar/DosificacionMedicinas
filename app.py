import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    dbname='nombre_de_base_de_datos',  # Reemplaza con el nombre real de tu base de datos
    user='kebecerra@uts.edu.co',  # Reemplaza con tu usuario
    password='tu_contraseña',  # Reemplaza con tu contraseña
    host='dosificacion.postgres.database.azure.com',  # Reemplaza con el host correcto
    port='5432',
    sslmode='require'
)

@app.route('/')
def home():
    return "¡Hola, mundo!"

@app.route('/medicamentos', methods=['GET'])
def obtener_medicamentos():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM medicamentos;")  # Suponiendo que tienes una tabla 'medicamentos'
        rows = cursor.fetchall()
        return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
