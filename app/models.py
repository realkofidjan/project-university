# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Student(UserMixin, db.Model):
    """
    Create an Student table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    student_id = db.relationship('Course_Student', backref='student',
                                lazy='dynamic')

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Student: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    dep_head = db.Column(db.String(60), unique=True)
    instructors = db.relationship('Instructor', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Course(db.Model):
    """
    Create a Course table
    """

    __tablename__ = 'courses'

    id = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(60), unique=True)
    instructor_name = db.Column(db.String(60), db.ForeignKey('instructors.name'))
    course_students = db.relationship('Course_Student', backref='course',
                                lazy='dynamic')

    def __repr__(self):
        return '<Course: {}>'.format(self.name)

class Course_Student(db.Model):
    """
    Create a Course_Student table
    """

    __tablename__ = 'course_students'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(3), db.ForeignKey('courses.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __repr__(self):
        return '<Course_Student: {}>'.format(self.name)


class Instructor(db.Model):
    """
    Create a Instructor table
    """

    __tablename__ = 'instructors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    department_name = db.Column(db.String(60), db.ForeignKey('departments.name'))
    instructor_id = db.relationship('Course', backref='instructor',
                                lazy='dynamic')

    def __repr__(self):
        return '<Instructor: {}>'.format(self.name)


