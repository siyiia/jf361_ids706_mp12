from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a + b})
    except ValueError:
        return jsonify({'error': 'Invalid input, please provide numbers'}), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a - b})
    except ValueError:
        return jsonify({'error': 'Invalid input, please provide numbers'}), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a * b})
    except ValueError:
        return jsonify({'error': 'Invalid input, please provide numbers'}), 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 1))  # Default b to 1 to avoid division by zero
        if b == 0:
            return jsonify({'error': 'Division by zero is not allowed'}), 400
        return jsonify({'result': a / b})
    except ValueError:
        return jsonify({'error': 'Invalid input, please provide numbers'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
