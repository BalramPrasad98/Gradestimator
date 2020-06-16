import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
# django.setup()

from Profiles.models import Transcript

import pandas as pd

def create_allstudents_dataframe():

    AllTranscripts = Transcript.objects.all()
    df = pd.DataFrame(columns=['Student', 'Course', 'Grade'])

    # Populate the DataFrame
    for student in AllTranscripts:

        df = df.append({'Student': student.Student,
        'Course': student.Course,
        'Grade': student.Transcript_Grade},
        ignore_index=True)

    return df

total_df = create_allstudents_dataframe()
