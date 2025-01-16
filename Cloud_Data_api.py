# cloud_api.py
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Endpoint for receiving sensor data
@app.route('/upload_data', methods=['POST'])
def upload_data():
    data = request.get_json()
    print(f"Received Data: {data}")
    # Here you would typically save the data to a database or cloud service
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
