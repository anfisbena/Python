import pyodbc


try:
    con_string =r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\arcil\Waypoint Global\GMAC OPPORTUNITIES - Documents\GMAC Opportunities 2021\Training\dummy.accdb;'                   #open the connection
    conn=pyodbc.connect(con_string) #create the connection
    cursor=conn.cursor()            #move over the database cursor
    myuser=(
        ('HUSBANDO',1,'Waypoint','USS Shot','Pto Tequila','Kasajstan','4','20','Happy service','04020','TON','400','20','caca'),
    )
    cursor.executemany ('INSERT INTO database_tbl VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',myuser)
    conn.commit()
    print('data inserted successfully')
except pyodbc.error as e:
    print('connection error', e)