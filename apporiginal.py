# Importing pakages
import streamlit as st
#import mysql.connector

from create import create
# from database import create_table
from delete import delete
from read import read
from update import update
from query import query1





def main():
    st.title("RESUME DETAILS (DBMS_PROJECT)")
    menu = ["Add", "Read", "Edit", "Remove","Query"]
    choice = st.sidebar.selectbox("Add/Read/Update/Delete/Query", menu)

    # create_table()
    if choice == "Add":
        st.subheader("Enter job Details:")
        create()

    elif choice == "Read":
        st.subheader("Read job details")
        read()

    elif choice == "Edit":
        st.subheader("Update job details")
        update()

    elif choice == "Remove":
        st.subheader("Delete job")
        delete()

    elif choice =="Query":
         st.subheader("query and extract data from tables")
         query1()
    
    # elif choice=="Function":
    #     st.subheader("Enter type of blood")
    #     function1()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()# Importing pakages
import streamlit as st
#import mysql.connector

from create import create
# from database import create_table
from delete import delete
from read import read
from update import update
from query import query1





def main():
    st.title("RESUME DETAILS app(PES1UG20CS120_DBMS_PROJECT)")
    menu = ["Add", "Read", "Edit", "Remove","Query"]
    choice = st.sidebar.selectbox("Add/Read/Update/Delete/Query", menu)

    # create_table()
    if choice == "Add":
        st.subheader("Enter job Details:")
        create()

    elif choice == "Read":
        st.subheader("Read job details")
        read()

    elif choice == "Edit":
        st.subheader("Update job details")
        update()

    elif choice == "Remove":
        st.subheader("Delete job")
        delete()

    elif choice =="Query":
         st.subheader("query and extract data from tables")
         query1()
    
    # elif choice=="Function":
    #     st.subheader("Enter type of blood")
    #     function1()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()