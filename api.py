from flask import Flask, jsonify, render_template_string
import psycopg2
from psycopg2 import sql

api = Flask(__name__)

# PSQL connection info:
conn = psycopg2.connect(
    dbname="dvdrental", 
    user="raywu1990", 
    password="test", 
    host="127.0.0.1", 
    port="5432"
)

@api.route('/api/update_basket_a')
def update_basket_a():
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
            conn.commit()
        return "Successfully Added items to basket"
    except Exception as e:
        return str(e)

@api.route('/api/unique')
def unique_fruits():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT DISTINCT fruit_a FROM basket_a")
            unique_a = [row[0] for row in cursor.fetchall()]
            
            cursor.execute("SELECT DISTINCT fruit_b FROM basket_b")
            unique_b = [row[0] for row in cursor.fetchall()]

        html = """
        <html>
        <body>
            <h2>Unique Fruits</h2>
            <table border="1">
                <tr><th>Unique in Basket A</th><th>Unique in Basket B</th></tr>
                <tr><td>{}</td><td>{}</td></tr>
            </table>
        </body>
        </html>
        """.format(', '.join(unique_a), ', '.join(unique_b))

        return render_template_string(html)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    api.run(debug=True)

