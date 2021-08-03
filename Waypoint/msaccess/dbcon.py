import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\arcil\Waypoint Global\GMAC OPPORTUNITIES - Documents\GMAC Opportunities 2021\Training\dummy.accdb;'
    conn= pyodbc.connect(con_string)
    print('connected')
except pyodbc.Error as e:
    print('error in connection, ', e)