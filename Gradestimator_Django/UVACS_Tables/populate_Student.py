# Configure settings for project
# Need to run this before calling models from application!

def __setup_django(root_path, settings):
    import os
    import django
    import sys

    os.chdir(root_path)

    # Django settings
    sys.path.append(root_path)
    os.environ['DJANGO_SETTINGS_MODULE'] = settings

    django.setup()

PROJECT_PATH = "/app"
PROJECT_SETTING = "Gradestimator_Django.settings"

__setup_django(PROJECT_PATH, PROJECT_SETTING)


import random
from UVACS_Tables.models import Student

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
    populate(1000)
    print('Students has been populated')
