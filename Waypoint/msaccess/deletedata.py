import pyodbc

try:
    con_string =r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\arcil\Waypoint Global\GMAC OPPORTUNITIES - Documents\GMAC Opportunities 2021\Training\dummy.accdb;'
    conn=pyodbc.connect(con_string)

    Case=1

    cursor=conn.cursor()
    cursor.execute ('DELETE * FROM Database_Tbl WHERE Case = ?',(Case))
    conn.commit()
    print ('Data updated successfully')



except pyodbc.error as e:
    print('connection error', e)