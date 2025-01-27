from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a route to get user details based on a user_id
@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Mock user data to be returned
    user_data = {
        "user_id": user_id,
        "name": "Vibhanshu Singh",
        "email": "vibhanshusingh@gmail.com"
    }

    # Check if the 'extra' parameter is provided in the request and add it to the response if available
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    # Return the user data as JSON with a 200 status code
    return jsonify(user_data), 200

# Define a route to create a user via a POST request
@app.route("/create-user", methods=["POST"])
def create_user():
    # Parse the JSON data from the incoming request
    data = request.get_json

    # Return the parsed data as JSON with a 201 status code
    return jsonify(data), 201

# Run the application in debug mode when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
