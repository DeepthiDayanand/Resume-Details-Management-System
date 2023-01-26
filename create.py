import streamlit as st
from database import add_data_job
from database import add_data_member
from database import add_data_school
from database import add_data_degree_info
from database import add_data_projects
from database import add_data_experience

#for job table
def create_job():
    col1, col2 = st.columns(2)
    with col1:
        JOB_ID = st.text_input("JOB_ID:")
        TITLE = st.text_input("TITLE:")
    with col2:
        LOCATION = st.text_input("LOCATION:")
        DESCRIPTION=st.text_input("DESCRIPTION:")
        EMPLOYER=st.text_input("EMPLOYER")

    if st.button("Add job details"):
        add_data_job(JOB_ID,TITLE,LOCATION,DESCRIPTION,EMPLOYER)
        st.success("Successfully added job: {} going to {}")

#for member table
def create_member():
    col1, col2 = st.columns(2)
    with col1:
        MEMBER_ID = st.text_input("MEMBER_ID:")
        PASSWORD = st.text_input("PASSWORD:")
        EMAIL = st.text_input("EMAIL:")
        NAME = st.text_input("NAME:")
        PHONE=st.text_input("PHONE:")
    with col2:
        ADDRESS=st.text_input("ADDRESS")
        BIO = st.text_input("BIO:")
        GITHUB = st.text_input("GITHUB:")
        LINKEDIN = st.text_input("LINKEDIN:")

    if st.button("Add member details"):
        add_data_member(MEMBER_ID,PASSWORD,NAME,EMAIL,PHONE, ADDRESS, BIO, GITHUB, LINKEDIN)
        st.success("Successfully added member: {} going to {}")

#for school table
def create_school():
    col1, col2 = st.columns(2)
    with col1:
        SCHOOL_ID = st.text_input("SCHOOL_ID:")
        LOCATION = st.text_input("LOCATION:")
        NAME=st.text_input("NAME:")

    if st.button("Add school details"):
        add_data_school(SCHOOL_ID, LOCATION, NAME)
        st.success("Successfully added school: {} going to {}")

#for degree_info table
def create_degree_info():
    col1, col2 = st.columns(2)
    with col1:
        DEGREE_ID = st.text_input("DEGREE_ID:")
        TYPE_OF_GRADUATION = st.text_input("TYPE_OF_GRADUATION:")
    with col2:
        DEGREE=st.text_input("DEGREE")
        MAJOR = st.text_input("MAJOR:")

    if st.button("Add degree details"):
        add_data_degree_info('DEGREE_ID', 'TYPE_OF_GRADUATION','DEGREE', 'MAJOR')
        st.success("Successfully added degree: {} going to {}")

#for projects table
def create_projects():
    col1, col2 = st.columns(2)
    with col1:
        MEMBER_ID = st.text_input("MEMBER_ID:")
        PROJECT_NAME = st.text_input("PROJECT_NAME:")
        DESCRIPTION=st.text_input("DESCRIPTION")

    if st.button("Add project details"):
        add_data_projects('MEMBER_ID', 'PROJECT_NAME','DESCRIPTION')
        st.success("Successfully added project: {} going to {}")

#for experience table
def create_experience():
    col1, col2 = st.columns(2)
    with col1:
        MEMBER_ID = st.text_input("MEMBER_ID:")
        JOB_ID = st.text_input("JOB_ID:")
    with col2:
        START_DATE=st.text_input("START DATE")
        END_DATE = st.text_input("END DATE:")

    if st.button("Add experience details"):
        add_data_experience('MEMBER_ID', 'JOB_ID', 'START_DATE', 'END_DATE')
        st.success("Successfully added experience: {} going to {}")