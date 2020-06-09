import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
django.setup()

from Profiles.models import Course


def populate(course_dict):
    Course.objects.all().delete()
    # Reads the course into the database
    for key in course_dict:
        Course.objects.get_or_create(Course_ID=key, Course_Name=course_dict[key])

# Dictionary of course and its corresponding name
Courses = {'CS 1110': 'Introduction to Computer Science',
'CS 2110': 'Software Development Methods', 'CS 2102': 'Discreet Mathematics',
'CS 2150': 'Program and Data Representation', 'CS 4102': 'Algorithms',
'CS 3330': 'Computer Architecture'}

if __name__ == '__main__':
    print("Populating Courses...Please Wait")
    populate(Courses)
    print('Courses has been populated')
