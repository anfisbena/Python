import pyodbc

try:
    con_string =r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\arcil\Waypoint Global\GMAC OPPORTUNITIES - Documents\GMAC Opportunities 2021\Training\dummy.accdb;'                   #open the connection
    conn=pyodbc.connect(con_string) #create the connection
    cursor=conn.cursor()            #move over the database cursor
    cursor.execute ('SELECT * FROM database_tbl')
    for row in cursor.fetchall():
        print(row)

except pyodbc.error as e:
    print('connection error', e)