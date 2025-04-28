

import pyodbc

connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESKTOP-L4RJI31;'
                               'Database=Roster;' 
                               'trusted_Connection=yes;'
                               )
print('Connected Successfully')

cursor = connection.cursor()

create = """create table Roster 
(
    Name Varchar(50), 
    Species varchar(50), 
    Age int
)
"""
insert = """insert into Roster
values
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29)
"""

cursor.execute(create)
cursor.execute(insert)

connection.commit()

cursor.execute("SELECT * FROM Roster")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
