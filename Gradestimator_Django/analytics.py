import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Gradestimator_Django.settings')

import django
# Import settings
# django.setup()

from Analytics.models import SignificantCourse
from Profiles.models import Student, Grade, Transcript, Prerequisite, Course
from django.contrib.auth.models import User

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


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

def runanalytics(myCourses):

    # Columns in df - ['Student', 'Course', 'Grade']
    total_df = create_allstudents_dataframe()
    # Get all of the significant courses and their corresponding grades
    Selected_Courses = myCourses

    # Get the first course and grade
    first_course = Selected_Courses[0].SigCourse
    first_grade = Selected_Courses[0].Grade

    # Finding the total students
    total_students = len(total_df.Student.unique())

    # Create a list of the subsetted students
    sub_students = total_df['Student'][(total_df['Course'] == first_course) & (total_df['Grade'] == first_grade)]
    # Create the initial subsetted frame
    sub_frame = total_df[total_df['Student'].isin(list(sub_students))]

    # If there is more than 1 significant course then subset for thos courses as well
    if len(Selected_Courses)>1:
        for i in range(1,len(Selected_Courses)):
            second_course = Selected_Courses[i].SigCourse
            second_grade = Selected_Courses[i].Grade

            temp_student = sub_frame['Student'][(sub_frame['Course'] == second_course) & (sub_frame['Grade'] == second_grade)]
            temp_frame = sub_frame[sub_frame['Student'].isin(list(temp_student))]
            sub_frame = temp_frame
        # Assign the final frame to our original subsetted frame
        sub_frame = temp_frame

    # Find the original course that we are predicting a grade for
    t3 = sub_frame['Course'] == Selected_Courses[0].Original_Course

    # Get the final frame
    final_frame = sub_frame[t3]

    # Significant students used for analytics
    significant_students = len(final_frame.Student.unique())

    # Get the values and the grades to input in the pie chart
    grades = final_frame.Grade.astype(str).value_counts().index.tolist()
    values = final_frame.Grade.value_counts().tolist()

    if not grades:
        return ("Unfortunately we could not find any students whose course history matched the one given.")
    # Highest Grade
    most_likely_grade = grades[0]
    predicted_course = Selected_Courses[0].Original_Course

    # Creating the Pie Chart
    fig = go.Figure(data=[go.Pie(labels=grades, values=values,
    textinfo='label+percent')])
    fig.update_layout(showlegend=False)
    return fig, most_likely_grade, predicted_course, total_students, significant_students


if __name__ == '__main__':
    runanalytics(SignificantCourse.objects.all())
