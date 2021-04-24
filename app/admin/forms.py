from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    dep_head = StringField('dep_head', validators=[DataRequired()])
    submit = SubmitField('Submit')

class InstructorForm(FlaskForm):
    """
    Form for admin to add or edit an instructor
    """
    name = StringField('Name', validators=[DataRequired()])
    department_name = StringField('department_name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    """
    Form for admin to add or edit a course
    """
    id = StringField('id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    instructor_name = StringField('instructor_name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    """
    Form for admin to add or edit an instructor
    """
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Submit')