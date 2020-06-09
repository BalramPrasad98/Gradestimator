import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
django.setup()

import random
from Profiles.models import Student

def populate(students=100):
    # Clear the student table
    Student.objects.all().delete()

    # Create a list of unique student pins. Possible pins are 1.5 times the
    # number of total students
    student_pin_list = []
    for i in range(1,students):
        student_pin_list = random.sample((range(1, (int(students*1.5)))), students)
    # Input the pins and year for all students
    for p in student_pin_list:
        Student.objects.get_or_create(Student_ID=p, Student_Year='Senior')


if __name__ == '__main__':
    print("Populating Students...Please Wait")
    populate(500)
    print('Students has been populated')
