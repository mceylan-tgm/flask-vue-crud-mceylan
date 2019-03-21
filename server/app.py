import os
import uuid


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS


# configuration

# instantiate the app
app = Flask(__name__)
# enable CORS
CORS(app)
auth = HTTPBasicAuth()


USER = [
    { 'id': uuid.uuid4().hex, "username": "mceylan2", "email": "mceylan2@tgm.ac.at", "image": "bild.jpg"},
    { 'id': uuid.uuid4().hex, "username": "eecevit", "email": "eecevit@email.com", "image": "null"},
    { 'id': uuid.uuid4().hex, "username": "mceylan", "email": "mceylan@email.com", "image": "null"}]


users = {
    "mceylan": "secret",
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# sanity check route

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/user', methods=['GET', 'POST'])
@auth.login_required
def all_user():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        USER.append({
            'id': uuid.uuid4().hex,
            'username': post_data.get('username'),
            'email': post_data.get('email'),
            'image': post_data.get('image'),
        })
        response_object['message'] = 'User added!'
    else:
        response_object['user'] = USER
    return jsonify(response_object)


@app.route('/user/<book_id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        # TODO: refactor to a lambda and filter
        return_book = ''
        for book in USER:
            if book['id'] == book_id:
                return_book = book
        response_object['book'] = return_book
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        USER.append({
            'id': uuid.uuid4().hex,
            'username': post_data.get('username'),
            'email': post_data.get('email'),
            'image': post_data.get('image'),
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

@auth.login_required
def remove_book(user_id):
    for book in USER:
        if book['id'] == user_id:
            USER.remove(book)
            return True
    return False


if __name__ == '__main__':
    app.run()
