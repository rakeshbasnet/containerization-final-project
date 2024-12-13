from app import app
from flask import Flask, request, redirect, url_for, render_template, jsonify
from app.db import user_collection


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/api/users', methods=['GET'])
def get_users():
     users = list(user_collection.find())
     users_list = []
     for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
        users_list.append(user)

     return jsonify(users_list)


@app.route('/api/add-user', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    new_user = request.get_json()

    user_collection.insert_one(new_user)
    return 'User Added'
