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

from Demo_UVACS.models import Student, Course, Grade, Transcript
import random

# Function to generate a grade based on a course ID and distribution
# Grades breakdown is used from vagrades.com
def generate_grade(c):
    grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
    breakdown = []
    if (c == 'CS 1110: Introduction to Computer Science'):
        breakdown = [341,2479,1397,1133,796,441,269,199,126,65,41,27,54]
        denom = sum(breakdown)
        distribution = [b / denom for b in breakdown]
        r = random.choices(grades, distribution)
        return r[0]
    elif (c == 'CS 2110: Software Development Methods'):
        breakdown = [658,1887,978,720,606,282,158,131,61,35,30,11,59]
        denom = sum(breakdown)
        distribution = [b / denom for b in breakdown]
        r = random.choices(grades, distribution)
        return r[0]
    elif (c == 'CS 2102: Discreet Mathematics'):
        # Need to update
        breakdown = [402,1186,650,535,602,284,197,215,79,39,70,36,55]
        denom = sum(breakdown)
        distribution = [b / denom for b in breakdown]
        r = random.choices(grades, distribution)
        return r[0]
    elif (c == 'CS 2150: Program and Data Representation'):
        # Need to update
        breakdown = [105,955,527,509,521,297,252,246,123,67,68,65,214]
        denom = sum(breakdown)
        distribution = [b / denom for b in breakdown]
        r = random.choices(grades, distribution)
        return r[0]
    elif (c == 'CS 4102: Algorithms'):
        # Need to update
        breakdown = [160,577,379,318,343,226,132,124,79,21,27,25,40]
        denom = sum(breakdown)
        distribution = [b / denom for b in breakdown]
        r = random.choices(grades, distribution)
        return r[0]
    elif (c == 'CS 3330: Computer Architecture'):
        # Need to update
        breakdown = [83,332,353,401,335,250,195,114,68,31,26,13,35]
        denom = sum(breakdown)
        distribution = [b / denom for b in breakdown]
        r = random.choices(grades, distribution)
        return r[0]
    else:
        return 'No Grade'



# Populate the Transcript table.
def populate():
    # Clear the transcript table
    Transcript.objects.all().delete()
    # Get all of the available students
    AllStudents = Student.objects.all()
    # Get all of the available courses
    AllCourses = Course.objects.all()
    # Assume each student has taken each course and give a random grade that
    # corresponds to that courses distribution
    for s in AllStudents:
        for c in AllCourses:
            Transcript.objects.create(Student=s,
            Course=c, Transcript_Grade = Grade.objects.get(Letter_Grade=generate_grade(str(c))))




if __name__ == '__main__':
    print("Populating Transcripts...Please Wait")
    populate()
    print('Transcripts has been populated')

    # CODE TO MAKE SURE ALL COURSES HAVE A GRADE - SHOULD BE EMPTY SET
    # print(Transcript.objects.filter(Transcript_Grade='No Grade'))
