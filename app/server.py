from flask import Flask, jsonify, request
import db
app = Flask(__name__)

# welcome to myworld
@app.route('/')
def hello_world():
    return '<p> WELCOME TO MY WORLD  </p>'

# a GET request to /user/ returns a list of registered users on a system
@app.route('/user/', methods=['GET'])
def get_userAll():
    return jsonify(db.get_all())

#a GET request to /user/123 returns the details of user 123
@app.route('/user/<uid>', methods=['GET'])
def get_users(uid):
    jsonData = db.get_data(uid)
    return jsonify(jsonData)

# a POST request to /user/new creates a user with the using the body data. The response returns the ID.
@app.route('/user/new', methods=['POST'])
def create_user():
    uid = request.json['uid']
    name = request.json['name']
    age = request.json['age']
    db.insert_data(uid, name, age)
    return jsonify({'message': 'User created successfully!'})

# a PUT request to /user/123 updates user 123 with the body data 
@app.route('/user/<uid>', methods=['PUT'])
def update_user(uid):
    name = request.json['name']
    age = request.json['age']
    db.update_date(uid, name, age)
    return jsonify({'message': 'User updated successfully!'})

# a DELETE request to /user/123 deletes user 123
@app.route('/user/<uid>', methods=['DELETE'])
def delete_user(uid):
    db.delete_date(uid)
    return jsonify({'message': 'User deleted successfully!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)