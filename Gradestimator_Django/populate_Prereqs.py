import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
django.setup()

from Profiles.models import Prerequisite, Course

def populate(requisites):
    # Clear the prerequisite table
    Prerequisite.objects.all().delete()
    # Create a dictionary of the courses and the corresponding prerequsites

    for k in requisites:
        # Req_object_dict.update({Course.objects.get(Course_ID=k[0]): Course.objects.get(Course_ID=k[1])})
        Prerequisite.objects.get_or_create(
        Desired_Course=Course.objects.get(Course_ID=k[0]),
        Course_Prerequisite=Course.objects.get(Course_ID=k[1]))
    # Put the prerequisites into the database
    

# Dictionary of courses and their corresponding prerequisites
Prerequisites_dict = (('CS 2102', 'CS 1110'), ('CS 2110', 'CS 1110'),
('CS 2150', 'CS 2110'), ('CS 2150', 'CS 2102'), ('CS 4102', 'CS 2150'),
('CS 3330', 'CS 2150'))


if __name__ == '__main__':
    print("Populating Prerequisites...Please Wait")
    populate(Prerequisites_dict)
    print('Prerequisites has been populated')
