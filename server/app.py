# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db, Employee, Meeting, Project, Assignment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/employees')
def get_employees():
    employees = Employee.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'hire_date': str(e.hire_date)} for e in employees])

@app.route('/employees/<int:id>/meetings')
def get_employee_meetings(id):
    employee = Employee.query.get_or_404(id)
    return jsonify([{'id': m.id, 'topic': m.topic} for m in employee.meetings])

@app.route('/employees/<int:id>/projects')
def get_employee_projects(id):
    employee = Employee.query.get_or_404(id)
    return jsonify([{'id': p.id, 'title': p.title} for p in employee.projects])

@app.route('/projects/<int:id>/employees')
def get_project_employees(id):
    project = Project.query.get_or_404(id)
    return jsonify([{'id': e.id, 'name': e.name} for e in project.employees])


if __name__ == '__main__':
    app.run(port=5555, debug=True)
