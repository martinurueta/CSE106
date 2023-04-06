from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jomama_university.db'
app.config['SECRET_KEY'] = 'cringe'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    teacher = db.Column(db.String(120), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    totalStudent = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(120), nullable=False)
    enrollments = db.relationship('Enrollment', backref='class', lazy=True)

    def students_enrolled(self):
        return len(self.enrollments)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    grade = db.Column(db.String(80), nullable=True)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['user_role'] = user.role

        if user.role == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif user.role == 'teacher':
            return redirect(url_for('teacher_dashboard'))
        elif user.role == 'student':
            return redirect(url_for('student_dashboard'))
    else:
        return render_template('index.html', error='Invalid username or password')

@app.route('/add_user', methods=['POST'])
def add_user():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('index'))

    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    name = request.form.get('name')

    user = User(username=username, password=generate_password_hash(password), role=role, name=name)
    db.session.add(user)
    db.session.commit()

    return '', 200

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('index'))

    user_id = request.form.get('user_id')
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return '', 200
    else:
        return 'User not found', 404

@app.route('/add_class', methods=['POST'])
def add_class():
    # Add authentication and validation checks here

    name = request.form.get('name')
    teacher = request.form.get('teacher')
    capacity = request.form.get('capacity')
    time = request.form.get('time')

    new_class = Class(name=name, teacher=teacher, capacity=capacity, totalStudent=0, time=time)
    db.session.add(new_class)
    db.session.commit()

    return '', 200

@app.route('/delete_class', methods=['POST'])
def delete_class():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('index'))

    class_id = request.form.get('class_id')
    class_to_delete = Class.query.get(class_id)
    if class_to_delete:
        db.session.delete(class_to_delete)
        db.session.commit()
        return '', 200
    else:
        return 'Class not found', 404



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_role', None)
    return redirect(url_for('index'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('index'))
    users = User.query.all()
    classes = Class.query.all()
    enrollments = Enrollment.query.all()

    return render_template('admin_dashboard.html', users=users, classes=classes, enrollments=enrollments)

@app.route('/teacher_dashboard')
def teacher_dashboard():
    if 'user_id' not in session or session['user_role'] != 'teacher':
        return redirect(url_for('index'))
    teacher_name = User.query.filter_by(id=session['user_id']).first().name

    # Query the classes taught by the teacher
    classes = Class.query.filter_by(teacher=teacher_name).all()

    # Render the teacher_dashboard template with the classes
    return render_template('teacher_dashboard.html', classes=classes)


@app.route('/get_students_and_grades', methods=['POST'])
def get_students_and_grades():
    class_id = request.json.get('class_id')
    
    # Fetch enrollments and related student information for the given class
    enrollments = db.session.query(Enrollment, User).join(User).filter(Enrollment.class_id == class_id).all()

    # Prepare the list of students and their grades
    students_and_grades = []
    for enrollment, student in enrollments:
        students_and_grades.append({
            'id': student.id,
            'name': student.name,
            'grade': enrollment.grade
        })

    # Return the list of students and their grades as a JSON response
    return jsonify(students_and_grades)

@app.route('/update_student_grade', methods=['POST'])
def update_student_grade():
    if 'user_id' not in session or session['user_role'] != 'teacher':
        return redirect(url_for('index'))

    student_id = request.json.get('student_id')
    class_id = request.json.get('class_id')
    new_grade = request.json.get('new_grade')

    enrollment = Enrollment.query.filter_by(student_id=student_id, class_id=class_id).first()

    if enrollment:
        enrollment.grade = new_grade
        db.session.commit()
        return '', 200
    else:
        return 'Error updating grade', 400


@app.route('/student_dashboard')
def student_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Get the current user
    current_user = User.query.get(session['user_id'])

    # Get the classes the user is enrolled in
    enrolled_classes = Class.query.join(Enrollment, Class.id == Enrollment.class_id).filter(Enrollment.student_id == current_user.id).all()

    # Get all classes
    all_classes = Class.query.all()

    return render_template('student_dashboard.html', enrolled_classes=enrolled_classes, all_classes=all_classes)

@app.route('/enroll', methods=['POST'])
def enroll():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user_id = session['user_id']
    class_id = request.json.get('class_id')

    enrollment = Enrollment(student_id=user_id, class_id=class_id)  # Update student to student_id
    db.session.add(enrollment)
    db.session.commit()

    return '', 200


@app.route('/unenroll', methods=['POST'])
def unenroll():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user_id = session['user_id']
    class_id = request.json.get('class_id')

    enrollment = Enrollment.query.filter_by(student_id=user_id, class_id=class_id).first()  # Update student to student_id

    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        return '', 200
    else:
        return 'Error unenrolling', 400


if __name__ == '__main__':
    with app.app_context():
        # Create tables
        db.create_all()

        # Add an admin user
        admin_username = "jeff"  # Replace with the desired admin username
        admin_name = "Jeff"  # Replace with the desired admin name
        admin_password = "lov123"  # Replace with the desired admin password
        admin_role = "admin"

        existing_admin = User.query.filter_by(username=admin_username).first()
        if not existing_admin:
            hashed_password = generate_password_hash(admin_password)
            admin = User(username=admin_username, password=hashed_password, role=admin_role, name=admin_name)
            db.session.add(admin)
            db.session.commit()
            print("Admin user added.")

    app.run(debug=True)

