from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME"),
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT DATABASE() AS db_name;")
        result = cursor.fetchone()
        conn.close()
        return jsonify({"message": "Backend is working!", "database": result["db_name"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
