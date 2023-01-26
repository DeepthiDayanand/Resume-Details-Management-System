import datetime
import pandas as pd
import streamlit as st

from database import view_all_data_job, edit_dealer_data_job
from database import view_all_data_member, edit_dealer_data_member
from database import view_all_data_school, edit_dealer_data_school
from database import view_all_data_degree_info, edit_dealer_data_degree_info
from database import view_all_data_projects, edit_dealer_data_projects
from database import view_all_data_experience, edit_dealer_data_experience

#for table job
def update_job():
    result = view_all_data_job()
    # st.write(result)
    df = pd.DataFrame(result, columns=['JOB_ID', 'TITLE', 'LOCATION', 'DESCRIPTION','EMPLOYER'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_job_id = st.text_input("Job_id:")
            
        with col2:
            new_description = st.text_input("Description:")

        if st.button("Update desription"):
            edit_dealer_data_job(up_job_id,new_description)

            st.success("Successfully updated")

    result2 = view_all_data_job()
    df2 = pd.DataFrame(result2, columns=['JOB_ID', 'TITLE', 'LOCATION', 'DESCRIPTION','EMPLOYER'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table member
def update_member():
    result = view_all_data_member()
    # st.write(result)
    df = pd.DataFrame(result, columns=['MEMBER_ID','PASSWORD','NAME','EMAIL','PHONE', 'ADDRESS', 'BIO', 'GITHUB', 'LINKEDIN'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_member_id = st.text_input("Member_id:")
            
        with col2:
            new_name = st.text_input("Name:")

        if st.button("Update description"):
            edit_dealer_data_member(up_member_id,new_name)

            st.success("Successfully updated")

    result2 = view_all_data_member()
    df2 = pd.DataFrame(result2, columns=['MEMBER_ID','PASSWORD','NAME','EMAIL','PHONE', 'ADDRESS', 'BIO', 'GITHUB', 'LINKEDIN'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table school
def update_school():
    result = view_all_data_school()
    # st.write(result)
    df = pd.DataFrame(result, columns=['SCHOOL_ID', 'LOCATION', 'NAME'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_school_id = st.text_input("School_id:")
            
        with col2:
            new_name = st.text_input("Name:")

        if st.button("Update name"):
            edit_dealer_data_school(up_school_id,new_name)

            st.success("Successfully updated")

    result2 = view_all_data_school()
    df2 = pd.DataFrame(result2, columns=['SCHOOL_ID', 'LOCATION', 'NAME'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table degree_info
def update_degree_info():
    result = view_all_data_degree_info()
    # st.write(result)
    df = pd.DataFrame(result, columns=['DEGREE_ID', 'TYPE_OF_GRADUATION', 'DEGREE', 'MAJOR'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_degree_id = st.text_input("Degree_id:")
            
        with col2:
            new_major = st.text_input("Major:")

        if st.button("Update Major"):
            edit_dealer_data_school(up_degree_id,new_major)

            st.success("Successfully updated")

    result2 = view_all_data_degree_info()
    df2 = pd.DataFrame(result2, columns=['DEGREE_ID', 'TYPE_OF_GRADUATION', 'DEGREE', 'MAJOR'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table projects
def update_projects():
    result = view_all_data_projects()
    df = pd.DataFrame(result, columns=['MEMBER_ID', 'PROJECT_NAME','DESCRIPTION'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_member_id = st.text_input("Member_id:")
            
        with col2:
            new_project = st.text_input("Project name:")

        if st.button("Update project"):
            edit_dealer_data_projects(up_member_id,new_project)

            st.success("Successfully updated")

    result2 = view_all_data_projects()
    df2 = pd.DataFrame(result2, columns=['MEMBER_ID', 'PROJECT_NAME','DESCRIPTION'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#for table experience
def update_experience():
    result = view_all_data_experience()
    df = pd.DataFrame(result, columns=['MEMBER_ID', 'JOB_ID', 'START_DATE', 'END_DATE'])
    with st.expander("Current Data"):
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            up_member_id = st.text_input("Member_id:")
            
        with col2:
            new_startdate = st.text_input("Start date:")
            new_enddate = st.text_input("End date:")

        if st.button("Update experience"):
            edit_dealer_data_experience(up_member_id,new_startdate, new_enddate)

            st.success("Successfully updated")

    result2 = view_all_data_experience()
    df2 = pd.DataFrame(result2, columns=['MEMBER_ID', 'JOB_ID', 'START_DATE', 'END_DATE'])
    with st.expander("Updated data"):
        st.dataframe(df2)