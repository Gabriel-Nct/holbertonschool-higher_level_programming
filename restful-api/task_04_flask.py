#!/usr/bin/python3
"""
API using Flask
Users are stored in memory and managed via Flask routes.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Handle route for the root URL (“/”)

    Returns:
        str: Welcome to the Flask API!
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Set the Status

    Returns:
        str: "OK"
    """
    return "OK"


@app.route("/data")
def data():
    """
    Data stored in the API.

    Returns:
        JSON: A list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Data of users

    Args:
        username (str): The username to search

    Returns:
        JSON: User details if found, otherwise an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user

    Request:
        JSON containing "username", "name", "age", and "city".

    Returns:
        JSON: Confirmation message and added user details.
        If "username" is missing, returns an error message.
    """
    global users
    retrieved_data = request.get_json()

    if not retrieved_data or "username" not in retrieved_data:
        return jsonify({"error": "Username is required"}), 400

    username = retrieved_data["username"]
    users[username] = retrieved_data

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
