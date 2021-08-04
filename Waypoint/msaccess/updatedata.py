import pyodbc

try:
    con_string =r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\arcil\Waypoint Global\GMAC OPPORTUNITIES - Documents\GMAC Opportunities 2021\Training\dummy.accdb;'                   #open the connection
    conn=pyodbc.connect(con_string) #create the connection
    
    newdata = "HUSBANDING"
    Case = 1

    cursor=conn.cursor()
    cursor.execute ('UPDATE Database_Tbl SET Business = ? WHERE Case = ?',(newdata,Case))
    conn.commit()
    print ('Data updated successfully')

except pyodbc.error as e:
    print('connection error', e)

cursor.close()
conn.close()