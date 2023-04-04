from flask import Flask, jsonify, render_template, request
import flask_cors, json

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/')
def index():
    return render_template('grades.html')


@app.route('/grades', methods=['GET'])
@flask_cors.cross_origin()
def get_grades():
    try:
        with open('grades.json') as f:
            data = json.load(f)
    except:
        data = {}
    return jsonify(data)


@app.route('/grades/<name>', methods=['GET'])
@flask_cors.cross_origin()
def get_grade(name):
    try:
        with open('grades.json') as f:
            data = json.load(f)
    except:
        data = {}
    if name in data:
        return jsonify(data[name])
    else:
        return jsonify({'error': 'name not found'})


@app.route('/grades', methods=['POST'])
@flask_cors.cross_origin()
def post_grade():
    try:
        with open('grades.json') as f:
            data = json.load(f)
    except:
        data = {}

    name = request.json.get('name')
    grade = request.json.get('grade')

    if not name or not grade:
        return jsonify({'error': 'name or grade is empty'}), 400

    if name in data:
        return jsonify({'error': 'name already exists'})
    else:
        data[name] = grade
        with open('grades.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)


@app.route('/grades/<name>', methods=['PUT'])
@flask_cors.cross_origin()
def put_grade(name):
    try:
        with open('grades.json') as f:
            data = json.load(f)
    except:
        data = {}
    if name in data:
        data[name] = request.json['grade']
        with open('grades.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)
    else:
        return jsonify({'error': 'name not found'})


@app.route('/grades/<name>', methods=['DELETE'])
@flask_cors.cross_origin()
def delete_grade(name):
    try:
        with open('grades.json') as f:
            data = json.load(f)
    except:
        data = {}
    if name in data:
        del data[name]
        with open('grades.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)
    else:
        return jsonify({'error': 'name not found'})


if __name__ == '__main__':
    app.run()
