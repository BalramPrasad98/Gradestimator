import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
django.setup()

from Profiles.models import Transcript
import pandas as pd

def create_allstudents_dataframe():

    AllTranscripts = Transcript.objects.all()

    # Populate the DataFrame

    tt = Transcript.objects.values()
    df = pd.DataFrame(tt)
    df.columns = ['id', 'Student', 'Course', 'Grade']
    df = df.drop(['id'], axis=1)
    df['Course'] = df['Course'].astype(str)
    print(df)
    return df

total_df = create_allstudents_dataframe()
