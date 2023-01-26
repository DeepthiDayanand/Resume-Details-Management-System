# Importing packages
import streamlit as st

from query import query1
from read import read_phones #procedure modification
from read import read_candidates #proc modification

#job table
from create import create_job
from read import read_job
from update import update_job
from delete import delete_job

#member table
from create import create_member
from read import read_member
from update import update_member
from delete import delete_member

#school table
from create import create_school
from read import read_school
from update import update_school
from delete import delete_school

#degree_info table
from create import create_degree_info
from read import read_degree_info
from update import update_degree_info
from delete import delete_degree_info

#projects table
from create import create_projects
from read import read_projects
from update import update_projects
from delete import delete_projects

# #experience table
# from create import create_experience
# from read import read_experience
# from update import update_experience
# from delete import delete_experience


def main():
    st.title("Resume Details Management System")

    menu1 = ["Add", "Read", "Edit", "Remove","Query","Procedure","Candidate/Skill list"]
    choice = st.sidebar.selectbox("Perform CRUD operations", menu1)

    menu2 = ["Job", "Member", "School", "Degree Information","Projects"]
    choice2 = st.sidebar.selectbox("Pick a table", menu2)

    # create_table()
    if choice == "Add":

        if choice2 == "Job":
            st.subheader("Enter job details:")
            create_job()
        
        elif choice2=="Member":
            st.subheader("Enter member details:")
            create_member()

        elif choice2=="School":
            st.subheader("Enter school details:")
            create_school()
            
        elif choice2=="Degree Information":
            st.subheader("Enter degree details:")
            create_degree_info()

        elif choice2=="Projects":
            st.subheader("Enter project details:")
            create_projects()

        # elif choice2=="Experience":
        #     st.subheader("Enter experience details:")
        #     create_experience()

    elif choice == "Read":
        
        if choice2 == "Job":
            st.subheader("Read job details")
            read_job()

        elif choice2=="Member":
            st.subheader("Read member details:")
            read_member()

        elif choice2=="School":
            st.subheader("Read school details:")
            read_school()

        elif choice2=="Degree Information":
            st.subheader("Read degree details:")
            read_degree_info()

        elif choice2=="Projects":
            st.subheader("Read project details:")
            read_projects()

        # elif choice2=="Experience":
        #     st.subheader("Read experience details:")
        #     read_experience()

    elif choice == "Edit":

        if choice2 == "Job":
            st.subheader("Update job details")
            update_job()

        elif choice2=="Member":
            st.subheader("Update member details:")
            update_member()

        elif choice2=="School":
            st.subheader("Update school details:")
            update_school()

        elif choice2=="Degree Information":
            st.subheader("Update degree details:")
            update_degree_info()
        
        elif choice2=="Projects":
            st.subheader("Update project details:")
            update_projects()

        # elif choice2=="Experience":
        #     st.subheader("Update experience details:")
        #     update_experience()

    elif choice == "Remove":

        if choice2 == "Job":
            st.subheader("Delete job")
            delete_job()

        elif choice2=="Member":
            st.subheader("Delete member:")
            delete_member()

        elif choice2=="School":
            st.subheader("Delete school:")
            delete_school()

        elif choice2=="Degree Information":
            st.subheader("Delete degree details:")
            delete_degree_info()

        elif choice2=="Projects":
            st.subheader("Delete project details:")
            delete_projects()
        
        # elif choice2=="Experience":
        #     st.subheader("Delete experience details:")
        #     delete_experience()

    elif choice =="Query":
         st.subheader("Extract data from tables using sql queries:")
         query1()

    elif choice == "Procedure":
        st.subheader("Example for procedure")
        read_phones()

    elif choice == "Candidate/Skill list":
        st.subheader("Given below are a few candidates")
        read_candidates()


    else:
        st.subheader("About tasks")

if __name__ == '__main__':
    main()