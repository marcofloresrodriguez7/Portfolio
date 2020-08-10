import mysql.connector

# Adjusted Personal MySQL-Python Project, referencing Coursera MySQL Project.


# After the database-who is created (reference the following comment lines), and add the database attribute to the
# connector.
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin1",
    database = "who"
)

cursor = conn.cursor()

# To create database-who, uncomment line below, and add the database attribute to the connector; comment back after
# the database has been created.
# cursor.execute("CREATE DATABASE who")

# To create a table for the data, uncomment lines below; comment back after the table has been created.
#sql = ("CREATE TABLE who_table (Country VARCHAR(70),  Region VARCHAR(50), LEMale INTEGER(10), LEFemale INTEGER(10),"
       #"HALEMale INTEGER(10), HALEFemale INTEGER(10), PDPMale INTEGER(10), PDPFemale INTEGER(10), PDB5 INTEGER(10),"
       #"PDB28 INTEGER(10), MaternalMor VARCHAR(255))")
#cursor.execute(sql)
#conn.commit()


# Opening csv file and importing data.
file_handle = open(r"C:\mysql\whostat2005_mortality.csv", 'r')
Raw_data = file_handle.readlines()
# first 7 lines are the titles of each column, and last lines are text.
del Raw_data[:7]
del Raw_data[192:]

# Seperating data row by row to obtain the needed data; and propagating database row by row with needed data.
for rawstring in Raw_data:
    Number, blank1, Country, Region, blank2, LEMale, LEFemale, HALEMale, HALEFemale, PDPMale, PDPFemale, PDB5, PDB28,\
    MaternalMor, blank3, blank4, blank5, blank6, blank7, blank8, blank9 = rawstring.split(',', 20)

    # To initially propagate the who table, uncomment the following lines; comment back after the table has been
    # propagated.
    #sql = ("INSERT INTO who_table(Country, Region, LEMale, LEFemale, HALEMale, HALEFemale, PDPMale, PDPFemale, PDB5,"
           #"PDB28, MaternalMor) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    #values = (Country, Region, LEMale, LEFemale, HALEMale, HALEFemale, PDPMale, PDPFemale, PDB5, PDB28, MaternalMor)
    #cursor.execute(sql, values)
    #conn.commit()

sql = "SELECT * from who_table"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
