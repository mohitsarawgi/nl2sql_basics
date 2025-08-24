import sqlite3

# SQLite - serverless, Using this just to understand the basics 

connection = sqlite3.connect("DGIS.db")


## Creating cursor object to insert record, create table and retrive
cursor=connection.cursor()


# Cursor ye hota hai dekho -- 

# In SQLite, a cursor is an object that facilitates 
# interaction with the database. It serves as a temporary 
# control structure that allows for the execution of SQL queries
# and the retrieval of results, typically on a row-by-row basis.



# Table 1
table_info = """

Create TABLE DGIS(NAME VARCHAR(25), DEPARTMENT VARCHAR(25), salary INT);

"""

cursor.execute(table_info)

# Insert Some  Records

cursor.execute('''Insert Into DGIS values('Mohit', 'AI-ML', 35000)''')
cursor.execute('''Insert Into DGIS values('X', 'AI-ML', 30000)''')
cursor.execute('''Insert Into DGIS values('Y', 'Backend', 25000)''')
cursor.execute('''Insert Into DGIS values('Z', 'Frontend', 25000)''')


print("The inserted records are")

data = cursor.execute('''Select * From DGIS''')


# chal bhai saari rows dekh ab

for row in data:
    print(row)

# ab connection close kuki agar nhi tho error milega

connection.commit()
connection.close()

# dekho - python3 sql.py run karte hi ek db add hojayega