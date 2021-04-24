from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import DepartmentForm, InstructorForm, CourseForm, StudentForm
from .. import db
from ..models import Department, Instructor, Course, Student


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data, dep_head=form.dep_head.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        department.dep_head = form.dep_head.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.dep_head=department.dep_head
    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")


# Instructor Views

@admin.route('/instructors', methods=['GET', 'POST'])
@login_required
def list_instructors():
    """
    List all instructors
    """
    check_admin()

    instructor = Instructor.query.all()

    return render_template('admin/instructors/instructors.html',
                           instructors=instructor, title="Instructors")


@admin.route('/instructors/add', methods=['GET', 'POST'])
@login_required
def add_instructor():
    """
    Add an instructor to the database
    """
    check_admin()

    add_instructor = True

    form = InstructorForm()
    if form.validate_on_submit():
        instructor = Instructor(name=form.name.data,
                                department_name=form.department_name.data)
        try:
            # add instructor to the database
            db.session.add(instructor)
            db.session.commit()
            flash('You have successfully added a new instructor.')
        except:
            # in case instructor name already exists
            flash('Error: instructor name already exists.')

        # redirect to instructors page
        return redirect(url_for('admin.list_instructors'))

    # load instructor template
    return render_template('admin/instructors/instructor.html', action="Add",
                           add_instructor=add_instructor, form=form,
                           title="Add Instructor")


@admin.route('/instructors/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_instructor(id):
    """
    Edit an instructor
    """
    check_admin()

    add_instructor = False

    instructor = Instructor.query.get_or_404(id)
    form = InstructorForm(obj=instructor)
    if form.validate_on_submit():
        instructor.name = form.name.data
        instructor.department_name = form.department_name.data
        db.session.commit()
        flash('You have successfully edited the instructor.')

        # redirect to the instructors page
        return redirect(url_for('admin.list_instructors'))

    form.name.data = instructor.name
    return render_template('admin/instructors/instructor.html', action="Edit",
                           add_instructor=add_instructor, form=form,
                           instructor=instructor, title="Edit Instructor")


@admin.route('/instructors/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_instructor(id):
    """
    Delete an instructor from the database
    """
    check_admin()

    instructor = Instructor.query.get_or_404(id)
    db.session.delete(instructor)
    db.session.commit()
    flash('You have successfully deleted the instructor.')

    # redirect to the instructors page
    return redirect(url_for('admin.list_instructor'))

    return render_template(title="Delete Instructor")


# Course Views

@admin.route('/courses', methods=['GET', 'POST'])
@login_required
def list_courses():
    """
    List all courses
    """
    check_admin()

    course = Course.query.all()

    return render_template('admin/courses/courses.html',
                           courses=course, title="Courses")


@admin.route('/courses/add', methods=['GET', 'POST'])
@login_required
def add_course():
    """
    Add an course to the database
    """
    check_admin()

    add_course = True

    form = CourseForm()
    if form.validate_on_submit():
        course = Course(id=form.id.data, name=form.name.data,
                                instructor_name=form.instructor_name.data)
        try:
            # add course to the database
            db.session.add(course)
            db.session.commit()
            flash('You have successfully added a new course.')
        except:
            # in case course name already exists
            flash('Error: course name already exists.')

        # redirect to course page
        return redirect(url_for('admin.list_courses'))

    # load course template
    return render_template('admin/courses/course.html', action="Add",
                           add_course=add_course, form=form,
                           title="Add Course")


@admin.route('/courses/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_course(id):
    """
    Edit a Course
    """
    check_admin()

    add_course = False

    course = Course.query.get_or_404(id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        course.id = form.id.data
        course.name = form.name.data
        course.instructor_name = form.instructor_name.data
        db.session.commit()
        flash('You have successfully edited the course.')

        # redirect to the courses page
        return redirect(url_for('admin.list_courses'))

    form.name.data = course.name
    return render_template('admin/courses/course.html', action="Edit",
                           add_course=add_course, form=form,
                           course=course, title="Edit Course")


@admin.route('/courses/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete_course(id):
    """
    Delete a course from the database
    """
    check_admin()

    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('You have successfully deleted the course.')

    # redirect to the course page
    return redirect(url_for('admin.list_courses'))

    return render_template(title="Delete Course")

# Student Views

@admin.route('/students', methods=['GET', 'POST'])
@login_required
def list_students():
    """
    List all students
    """
    check_admin()

    student = Student.query.all()

    return render_template('admin/students/students.html',
                           students=student, title="Students")


@admin.route('/students/add', methods=['GET', 'POST'])
@login_required
def add_student():
    """
    Add a student to the database
    """
    check_admin()

    add_student = True

    form = StudentForm()
    if form.validate_on_submit():
        student = Student(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data, 
                            email=form.email.data,)

        try:
            # add student to the database
            db.session.add(student)
            db.session.commit()
            flash('You have successfully added a new student.')
        except:
            # in case student name already exists
            flash('Error: student name already exists.')

        # redirect to student page
        return redirect(url_for('admin.list_students'))

    # load student template
    return render_template('admin/students/student.html', action="Add",
                           add_student=add_student, form=form,
                           title="Add Student")


@admin.route('/students/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    """
    Edit a student
    """
    check_admin()

    add_student = False

    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.username = form.username.data
        student.email = form.email.data
        db.session.commit()
        flash('You have successfully edited the student.')

        # redirect to the student page
        return redirect(url_for('admin.list_students'))

    form.username.data = student.username
    return render_template('admin/students/student.html', action="Edit",
                           add_student=add_student, form=form,
                           student=student, title="Edit student")


@admin.route('/students/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_student(id):
    """
    Delete a student from the database
    """
    check_admin()

    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('You have successfully deleted the student.')

    # redirect to the student page
    return redirect(url_for('admin.list_students'))

    return render_template(title="Delete Student")