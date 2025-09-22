#!/usr/bin/env python3

from app import app
from models import *

with app.app_context():
    print('Testing Employee-Meeting relationship:')
    employee1 = Employee.query.filter_by(id=1).first()
    print(f'Employee 1 meetings: {employee1.meetings}')
    
    meeting2 = Meeting.query.filter_by(id=2).first()
    print(f'Meeting 2 employees: {meeting2.employees}')
    
    print('\nTesting Employee-Project relationship through Assignment:')
    employee2 = Employee.query.filter_by(id=2).first()
    print(f'Employee 2 assignments: {employee2.assignments}')
    print(f'Employee 1 projects (via proxy): {employee1.projects}')
    
    project1 = Project.query.filter_by(id=1).first()
    print(f'Project 1 employees (via proxy): {project1.employees}')