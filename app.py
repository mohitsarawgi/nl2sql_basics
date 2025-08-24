import streamlit as st
import os
import sqlite3

import google.generativeai as mohitai

# Configure API Key
mohitai.configure(api_key="AIzaSyDum4JdWAv0lVIMd8H58cYOhaBR1J7GehY")


# To load model and provide sql query as response

def get_response(ques,ans):
    model=mohitai.GenerativeModel('gemini-1.5-flash') 
    response=model.generate_content([ans[0],ques])
    return response.text


## Function to retrive query from sql database

def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    # To return all rows
    for row in rows:
        print(row)
    return rows


# Promt
ans=[
    """
 the sql database has the name DGIS and has the following columns - 
 Name, Department, salary \n\n for example, \n ex 1 - How many entries of 
 records are present the SQL command will be something like SELECT COUNT(*) FROM DGIS;
 \n example 2 - tell me all the people in aiml department?, the sql command will be 
 something like SELECT * FROM DGIS WHERE DEPARTMENT=any department input;
 also sql code should not have '''in the beginning or endword in output

"""
]



# Streamlit --

st.set_page_config(page_title="Batao bs kya DGIS ka kya Retrive karna hai")
st.header("DGIS table ke baare me poocho bs...")
question = st.text_input("Input: ", key = "Input")
submit=st.button("Pooch bs bhai..")

# agar submit karoge tab...
if submit:
    response=get_response(question, ans)
    print(response)
    data=read_sql_query(response,"DGIS.db")
    st.subheader("Dekho ab response")
    for row in data:
        print(row)
        st.header(row)


