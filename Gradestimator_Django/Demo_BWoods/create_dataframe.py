import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
django.setup()

from .models import Transcript
import pandas as pd

def create_allstudents_dataframe():

    # Populate the DataFrame
    tt = list(Transcript.objects.values())
    df = pd.DataFrame(tt)
    df.columns = ['Course', 'Student', 'Grade', 'id']
    df = df.drop(['id'], axis=1)
    return df

total_df = create_allstudents_dataframe()
