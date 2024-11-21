from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Python application running in Docker!"})

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json()
    number = data.get('number', 0)
    result = number ** 2
    return jsonify({"input": number, "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)