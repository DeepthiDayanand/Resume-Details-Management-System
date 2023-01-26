import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dbms"
)
c = mydb.cursor()

#For job table
def add_data_job(JOB_ID,TITLE,LOCATION,DESCRIPTION,EMPLOYER):
    c.execute('INSERT INTO job VALUES (%s,%s,%s,%s,'
              '%s)',
              (JOB_ID,TITLE,LOCATION,DESCRIPTION,EMPLOYER))
    mydb.commit()

def view_all_data_job():
    c.execute('SELECT * FROM job')
    data = c.fetchall()
    return data

def edit_dealer_data_job(JOB_ID,DESCRIPTION):
    c.execute("UPDATE job SET DESCRIPTION=%s WHERE "
              "JOB_ID=%s", (DESCRIPTION,JOB_ID))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_job(JOB_ID):
    c.execute('DELETE FROM job WHERE JOB_ID="{}"'.format(JOB_ID))
    mydb.commit()

#For member table
def add_data_member(MEMBER_ID,PASSWORD,NAME,EMAIL,PHONE, ADDRESS, BIO, GITHUB, LINKEDIN):
    c.execute('INSERT INTO member VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (MEMBER_ID,PASSWORD,NAME,EMAIL,PHONE, ADDRESS, BIO, GITHUB, LINKEDIN))
    mydb.commit()

def view_all_data_member():
    c.execute('SELECT * FROM member')
    data = c.fetchall()
    return data

def edit_dealer_data_member(MEMBER_ID,NAME):
    c.execute("UPDATE member SET NAME=%s WHERE "
              "MEMBER_ID=%s", (NAME,MEMBER_ID))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_member(MEMBER_ID):
    c.execute('DELETE FROM member WHERE MEMBER_ID="{}"'.format(MEMBER_ID))
    mydb.commit()


#for school table
def add_data_school(SCHOOL_ID, LOCATION, NAME):
    c.execute('INSERT INTO school VALUES (%s,%s,'
              '%s)',
              (SCHOOL_ID, LOCATION, NAME))
    mydb.commit()

def view_all_data_school():
    c.execute('SELECT * FROM school')
    data = c.fetchall()
    return data

def edit_dealer_data_school(SCHOOL_ID,NAME):
    c.execute("UPDATE school SET NAME=%s WHERE "
              "SCHOOL_ID=%s", (NAME,SCHOOL_ID))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_school(SCHOOL_ID):
    c.execute('DELETE FROM school WHERE SCHOOL_ID="{}"'.format(SCHOOL_ID))
    mydb.commit()

#for degree_info table
def add_data_degree_info(DEGREE_ID, TYPE_OF_GRADUATION, DEGREE, MAJOR):
    c.execute('INSERT INTO degree_info VALUES (%s,%s,%s,'
              '%s)',
              (DEGREE_ID, TYPE_OF_GRADUATION, DEGREE, MAJOR))
    mydb.commit()

def view_all_data_degree_info():
    c.execute('SELECT * FROM degree_info')
    data = c.fetchall()
    return data

def edit_dealer_data_degree_info(DEGREE_ID,MAJOR):
    c.execute("UPDATE degree_info SET MAJOR=%s WHERE "
              "DEGREE_ID=%s", (MAJOR,DEGREE_ID))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_degree_info(DEGREE_ID):
    c.execute('DELETE FROM degree_info WHERE DEGREE_ID="{}"'.format(DEGREE_ID))
    mydb.commit()

#for projects table
def add_data_projects(MEMBER_ID, PROJECT_NAME, DESCRIPTION):
    c.execute('INSERT INTO projects VALUES (%s,%s,'
              '%s)',
              (MEMBER_ID, PROJECT_NAME, DESCRIPTION))
    mydb.commit()

def view_all_data_projects():
    c.execute('SELECT * FROM projects')
    data = c.fetchall()
    return data

def edit_dealer_data_projects(MEMBER_ID,DESCRIPTION):
    c.execute("UPDATE projects SET DESCRIPTION=%s WHERE "
              "MEMBER_ID=%s", (DESCRIPTION,MEMBER_ID))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_projects(MEMBER_ID):
    c.execute('DELETE FROM projects WHERE MEMBER_ID="{}"'.format(MEMBER_ID))
    mydb.commit()

#for experience table
def add_data_experience(MEMBER_ID, JOB_ID, START_DATE, END_DATE):
    c.execute('INSERT INTO experience VALUES (%s, %s,%s,'
              '%s)',
              (MEMBER_ID, JOB_ID, START_DATE, END_DATE))
    mydb.commit()

def view_all_data_experience():
    c.execute('SELECT * FROM experience')
    data = c.fetchall()
    return data

def edit_dealer_data_experience(MEMBER_ID,START_DATE):
    c.execute("UPDATE experience SET START_DATE=%s, END_DATE=%s WHERE "
              "MEMBER_ID=%s", (START_DATE,END_DATE,MEMBER_ID))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_experience(MEMBER_ID):
    c.execute('DELETE FROM experience WHERE MEMBER_ID="{}"'.format(MEMBER_ID))
    mydb.commit()

def procedure_call():
    c.callproc("view_phones")
    x = []
    for result in c.stored_results():
        members = result.fetchall()
        for phone in members:
            x.append(phone)
    return x

def proc_call():
    c.callproc("view_candidates")
    x = []
    for result in c.stored_results():
        skill = result.fetchall()
        for major in skill:
            x.append(major)
    return x

def query(q):
    
        c.execute(q)
        return c.fetchall()

