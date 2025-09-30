from flask import Flask, jsonify, request
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def hack_1():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['POST'])
def hack_2():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def hack_3():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def hack_4():
    return jsonify({'payload': 'success',
                    'error': False})
    

@app.route('/api/v1/users', methods=['GET'])
def hack_5():
    return jsonify ({'payload':[]})

@app.route('/api/v1/user', methods=['POST'])
def hack_6():
    email = request.args.get('email')
    name = request.args.get('name')
    
    return jsonify({
        'payload': {
            'email': email,
            'name': name
        }
    })


@app.route('/api/v1/user/add', methods=['POST'])
def hack_7():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id,
        }
       })

@app.route('/api/v1/user/create', methods=['POST'])
def hack_8():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id,
        }
    })
if __name__ == "__main__":
    app.run(debug=True)