from flask import Flask, jsonify, request
from services import user_service
from utils.custom_exceptions.user_exceptions import UserExceptions

app = Flask(__name__)


@app.route("/get-user/<username>")
def get_user(username):
    try:
        data = user_service.get_user(username)

        return jsonify(data), 201
    except UserExceptions as ex:
        return jsonify(ex.message), 502


@app.route("/create-user-profile", methods=["POST"])
def create_user_profile():
    try:
        user_input = request.get_json()
        data = user_service.create_user_profile(user_input["Username"], user_input["FirstName"],
                                                user_input["LastName"], user_input["Password"])
        return jsonify(data), 201
    except UserExceptions as ex:
        return jsonify(ex.message), 502


if __name__ == "__main__":
    app.run(debug=True)
