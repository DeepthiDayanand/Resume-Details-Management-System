import pandas as pd
import streamlit as st

from database import view_all_data_job, delete_data_job
from database import view_all_data_member, delete_data_member
from database import view_all_data_school, delete_data_school
from database import view_all_data_degree_info, delete_data_degree_info
from database import view_all_data_projects, delete_data_projects
from database import view_all_data_experience, delete_data_experience

#for table job
def delete_job():
    result = view_all_data_job()
    df = pd.DataFrame(result,columns=['JOB_ID', 'TITLE', 'LOCATION', 'DESCRIPTION','EMPLOYER'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_JOB=st.text_input("Enter job ID")

    if st.button("Delete job"):
        delete_data_job(selected_JOB)
        st.success("Job has been deleted successfully")
    new_result = view_all_data_job()
    df2 = pd.DataFrame(new_result, columns=['JOB_ID', 'TITLE', 'LOCATION', 'DESCRIPTION','EMPLOYER'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table member
def delete_member():
    result = view_all_data_member()
    df = pd.DataFrame(result,columns=['MEMBER_ID','PASSWORD','NAME','EMAIL','PHONE', 'ADDRESS', 'BIO', 'GITHUB', 'LINKEDIN'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_member=st.text_input("Enter Member ID")

    if st.button("Delete member"):
        delete_data_member(selected_member)
        st.success("Member has been deleted successfully")
    new_result = view_all_data_member()
    df2 = pd.DataFrame(new_result, columns=['MEMBER_ID','PASSWORD','NAME','EMAIL','PHONE', 'ADDRESS', 'BIO', 'GITHUB', 'LINKEDIN'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table school
def delete_school():
    result = view_all_data_school()
    df = pd.DataFrame(result,columns=['SCHOOL_ID', 'LOCATION', 'NAME'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_school=st.text_input("Enter School ID")

    if st.button("Delete school"):
        delete_data_school(selected_school)
        st.success("School has been deleted successfully")
    new_result = view_all_data_school()
    df2 = pd.DataFrame(new_result, columns=['SCHOOL_ID', 'LOCATION', 'NAME'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table degree_info
def delete_degree_info():
    result = view_all_data_degree_info()
    df = pd.DataFrame(result,columns=['DEGREE_ID', 'TYPE_OF_GRADUATION', 'DEGREE', 'MAJOR'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_degree=st.text_input("Enter Degree ID")

    if st.button("Delete degree"):
        delete_data_degree_info(selected_degree)
        st.success("Degree has been deleted successfully")
    new_result = view_all_data_degree_info()
    df2 = pd.DataFrame(new_result, columns=['DEGREE_ID', 'TYPE_OF_GRADUATION', 'DEGREE', 'MAJOR'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table projects
def delete_projects():
    result = view_all_data_projects()
    df = pd.DataFrame(result,columns=['MEMBER_ID', 'PROJECT_NAME','DESCRIPTION'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_project=st.text_input("Enter project name")

    if st.button("Delete project"):
        delete_data_projects(selected_project)
        st.success("Project has been deleted successfully")
    new_result = view_all_data_projects()
    df2 = pd.DataFrame(new_result, columns=['MEMBER_ID', 'PROJECT_NAME','DESCRIPTION'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table experience
def delete_experience():
    result = view_all_data_experience()
    df = pd.DataFrame(result,columns=['MEMBER_ID', 'JOB_ID', 'START_DATE', 'END_DATE'])
    with st.expander("Current data"):
        st.dataframe(df)

    selected_experience=st.text_input("Enter member ID")

    if st.button("Delete experience"):
        delete_data_experience(selected_experience)
        st.success("Experience has been deleted successfully")
    new_result = view_all_data_experience()
    df2 = pd.DataFrame(new_result, columns=['MEMBER_ID', 'JOB_ID', 'START_DATE', 'END_DATE'])
    with st.expander("Updated data"):
        st.dataframe(df2)