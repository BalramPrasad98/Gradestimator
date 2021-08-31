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


from Demo_UVACS.models import Grade


def populate(grade_dict):
    # Deletes the grades currently in the database
    Grade.objects.all().delete()
    # Reads the grades into the database
    for key in grade_dict:
        Grade.objects.get_or_create(Letter_Grade=key, Numerical_Weightage=grade_dict[key])

# Dictionary of grades and their weightage
Grades = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3,
'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'D-':0.7, 'F':0, 'No Grade':0}

if __name__ == '__main__':
    print("Populating Grades...Please Wait")
    populate(Grades)
    print('Grades has been populated')
