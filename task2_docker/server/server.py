import os
from flask import Flask, request, jsonify
from uuid import uuid4, UUID
from psycopg2 import pool

app = Flask(__name__)

connection_pool = pool.SimpleConnectionPool(
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ["POSTGRES_HOST"],
    port=os.environ["POSTGRES_PORT"],
    database="db",
    minconn=1,
    maxconn=10,
)


@app.route("/store", methods=["POST"])
def store_data():
    text_data = request.data.decode("utf-8")
    data_id = str(uuid4())
    with connection_pool.getconn() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO storage (id, text_data) VALUES (%s, %s);", (data_id, text_data)
        )
        conn.commit()
        connection_pool.putconn(conn)

    return jsonify(id=data_id), 200


@app.route("/retrieve/<data_id>", methods=["GET"])
def retrieve_data(data_id):
    try:
        UUID(data_id)
    except ValueError:
        return "Invalid data_id: not uuid format", 400

    with connection_pool.getconn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT text_data FROM storage WHERE id = %s;", (data_id,))
        result = cur.fetchone()
        connection_pool.putconn(conn)

    if result:
        return result[0], 200
    else:
        return "Data not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
