import streamlit as st
import sqlite3

conn =sqlite3.connect('student.db')
c=conn.cursor()

c.execute('''create table if not exists students 
          (id integer primary key autoincrement, name text, age integer)''')
conn.commit()

st.title("Student Manager with Streamlit + SQLITE3")

st.subheader("Add New Student")
name = st.text_input("Name")
age= st.number_input("Age",min_value=1)
if st.button("Add Student"):
    c.execute('insert into students (name,age) values (?,?)',(name,age))
    conn.commit()
    st.success(f"Student added: {name}")
    
st.subheader("View Student details")
if st.button("View"):
    c.execute('select * from students')
    data=c.fetchall()
    st.dataframe(data)
    

st.subheader("Remove Student details")
ID=st.number_input("Enter ID",min_value=1)
if st.button("Delete"):
    c.execute(f'delete from students where id={ID}')
    conn.commit()
    st.success(f'Student details removed,{ID}')

st.subheader("Update Student Details")
IDEN=st.number_input("Enter ID",min_value=1,max_value=100)
text_updation=st.text_input("Enter text updation")
if st.button("Update"):
    c.execute('update students set name=? where id=?',(text_updation,IDEN))
    conn.commit()
    st.success(f'Student details updated,{IDEN}')
    

    
    

