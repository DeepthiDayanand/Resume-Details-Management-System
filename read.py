import pandas as pd
import streamlit as st

from database import view_all_data_job
from database import view_all_data_member
from database import view_all_data_school
from database import view_all_data_degree_info
from database import view_all_data_projects
from database import view_all_data_experience 
from database import procedure_call
from database import proc_call 

#for job table
def read_job():
    result = view_all_data_job()
    #st.write(result)
    df = pd.DataFrame(result, columns=['JOB_ID', 'TITLE', 'LOCATION', 'DESCRIPTION','EMPLOYER'])
    with st.expander("View all Jobs"):
        st.dataframe(df)

#for member table
def read_member():
    result = view_all_data_member()
    #st.write(result)
    df = pd.DataFrame(result, columns=['MEMBER_ID','PASSWORD','NAME','EMAIL','PHONE', 'ADDRESS', 'BIO', 'GITHUB', 'LINKEDIN'])
    with st.expander("View all members"):
        st.dataframe(df)

#for procedure
def read_phones():
    result = procedure_call()
    #st.write(result)
    df = pd.DataFrame(result, columns=['MEMBER_ID','NAME','PHONE'])
    with st.expander("View all phones"):
        st.dataframe(df)

#for proc
def read_candidates():
    result = proc_call()
    #st.write(result)
    df = pd.DataFrame(result, columns=['MEMBER_ID','SKILL_NAME','EXPERIENCE_LEVEL/PREV EXPERIENCE', 'AREA OF EXPERTISE'])
    with st.expander("View all candidates"):
        st.dataframe(df)

#for school table
def read_school():
    result = view_all_data_school()
    #st.write(result)'MEM
    df = pd.DataFrame(result, columns=['SCHOOL_ID', 'LOCATION', 'NAME'])
    with st.expander("View all schools"):
        st.dataframe(df)

#for degree_info table
def read_degree_info():
    result = view_all_data_degree_info()
    df = pd.DataFrame(result, columns=['DEGREE_ID', 'TYPE_OF_GRADUATION', 'DEGREE', 'MAJOR'])
    with st.expander("View degree information"):
        st.dataframe(df)

#for projects table
def read_projects():
    result = view_all_data_projects()
    df = pd.DataFrame(result, columns=['MEMBER_ID', 'PROJECT_NAME','DESCRIPTION'])
    with st.expander("View project information"):
        st.dataframe(df)

#for experience table
def read_experience():
    result = view_all_data_experience()
    df = pd.DataFrame(result, columns=['MEMBER_ID', 'JOB_ID', 'START_DATE', 'END_DATE'])
    with st.expander("View experience information"):
        st.dataframe(df)