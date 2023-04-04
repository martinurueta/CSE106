from flask import Flask, jsonify, render_template, request
import flask_cors
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
flask_cors.CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grades.db'
db = SQLAlchemy(app)


class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {'name': self.name, 'grade': self.grade}

    def from_dict(self, data):
        for field in ['name', 'grade']:
            if field in data:
                setattr(self, field, data[field])
                
    @staticmethod
    def get_all_ordered_by_name():
        grades = Grade.query.order_by(Grade.name).all()
        return [{'name': grade.name, 'grade': grade.grade} for grade in grades]


with app.app_context(): 
    db.create_all()


@app.route('/')
def index():
    return render_template('grades.html')


@app.route('/grades', methods=['GET'])
@flask_cors.cross_origin()
def get_grades():
    grades = Grade.get_all_ordered_by_name()
    return jsonify(grades)




@app.route('/grades/<name>', methods=['GET'])
@flask_cors.cross_origin()
def get_grade(name):
    grade = Grade.query.filter_by(name=name).first()
    if grade:
        return jsonify(grade.to_dict())
    else:
        return jsonify({'error': 'name not found'})


@app.route('/grades', methods=['POST'])
@flask_cors.cross_origin()
def post_grade():
    name = request.json.get('name')
    grade = request.json.get('grade')

    if not name or not grade:
        return jsonify({'error': 'name or grade is empty'}), 400

    grade = Grade(name, grade)
    db.session.add(grade)
    db.session.commit()
    return jsonify(grade.to_dict())


@app.route('/grades/<name>', methods=['PUT'])
@flask_cors.cross_origin()
def put_grade(name):
    grade = Grade.query.filter_by(name=name).first()
    if grade:
        grade.from_dict(request.json)
        db.session.commit()
        return jsonify(grade.to_dict())
    else:
        return jsonify({'error': 'name not found'})


@app.route('/grades/<name>', methods=['DELETE'])
@flask_cors.cross_origin()
def delete_grade(name):
    grade = Grade.query.filter_by(name=name).first()
    if grade:
        db.session.delete(grade)
        db.session.commit()
        return jsonify(grade.to_dict())
    else:
        return jsonify({'error': 'name not found'})


if __name__ == '__main__':
    app.run()
