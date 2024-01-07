from flask import Flask, jsonify, request
import os
import mysql.connector

app = Flask(__name__)

# connector
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': 'users'
}

@app.route('/')
def test():
    return 'hello world'

@app.route('/create_table')
def create_table():
    conn = mysql.connector.connect(**db_config)
    cursor =  conn.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
        uid INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(80) UNIQUE NOT NULL,
        age INT(3) UNIQUE NOT NULL
    );
    """
    # Execute the CREATE TABLE query
    cursor.execute(create_table_query)
    conn.commit()
    return 'done'

def execute_query(query, data=None):
    conn = mysql.connector.connect(**db_config)
    cursor =  conn.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        conn.commit()
        return result
    finally:
        cursor.close()
        conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    query = "SELECT * FROM users;"
    result = execute_query(query)
    return jsonify(result)

@app.route('/users/<int:uid>', methods=['GET'])
def get_user(uid):
    query = "SELECT * FROM users WHERE uid = %s;"
    result = execute_query(query, (uid,))
    
    if result:
        return jsonify(result[0])
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    query = "INSERT INTO users (name, age) VALUES (%s, %s);"
    execute_query(query, (name, age))

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    query = "UPDATE users SET name = %s, age = %s WHERE uid = %s;"
    execute_query(query, (name, age, uid))

    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    query = "DELETE FROM users WHERE uid = %s;"
    execute_query(query, (uid,))

    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=True)
