import mysql.connector
controllers=[]
clients=[]
gateways=[]
services=[]
C_S=[]

#testing the conection of each client with the services 
def Check_DB():
    connection = mysql.connector.connect(host='localhost',
                                         database='yourdatabase',
                                         user='username',
                                         password='password')

    sql_select_Query = "select * from sdpid"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for row in records:
        if row[2]=='controller':
            controllers.append(row[0])
        if row[2]=='client':
            clients.append(row[0])
        if row[2]=='gateway':
            gateways.append(row[0])

    print('you have ',len(clients), 'clients') 
    
    sql_select_Query1 = "select * from sdpid_service"
    cursor1 = connection.cursor()
    cursor1.execute(sql_select_Query1)
    records1 = cursor1.fetchall()
    for row in records1:
        C_S.append(row[1])
#sending a note to the admin if there is a client not connected to any service
    for i, row in enumerate(records1):
        for sdpid in clients:

            if row[1] == sdpid:
                print("Client id= ",sdpid ," is connected to service id=",row[2])
    for sdpid in clients:
        if sdpid not in C_S:
            print ("NOTE:: Client id = ",sdpid," is not connected to any service")
    clients.clear()
    connection.commit()

def ADD_MACHINE():
    connection = mysql.connector.connect(host='localhost',
                                         database='yourdatabase',
                                         user='username',
                                         password='password')

    sql_select_Query = "select * from sdpid"
    MACHINE= input("Enter 'C' to add a Client machine, 'G' for gateway, and 'S' for Service: ")
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    New_Machine= len(records)+1
    if MACHINE == 'C':
       
        mycursor = connection.cursor()
        sql = "INSERT INTO sdpid(sdpid,valid,type,country,state,locality,org,org_unit,alt_name,email,serial)  VALUES (%s,1,'client','CA', 'ON', 'London', 'UWO', 'SE', 'Postdoc', 'abc@xyz.com', 'abc123')" %(New_Machine)
        mycursor.execute(sql)
        connection.commit()
        print(mycursor.rowcount, "record inserted.")
    elif MACHINE == 'G':

        mycursor = connection.cursor()
        sql = "INSERT INTO sdpid(sdpid,valid,type,country,state,locality,org,org_unit,alt_name,email,serial)  VALUES (%s,1,'gateway','CA', 'ON', 'London', 'UWO', 'SE', 'Postdoc', 'abc@xyz.com', 'abc123')" %(New_Machine)
        mycursor.execute(sql)
        connection.commit()
        print(mycursor.rowcount, "record inserted.")
def REMOVE_MACHINE():
    connection = mysql.connector.connect(host='localhost',
                                         database='sdp',
                                         user='root',
                                         password='2522')
    DELETE_ID = input("Enter the ID of the client you would like to remove: ")
    sql_select_Query = "DELETE FROM sdpid WHERE sdpid = %s" %(DELETE_ID)
    cursor=connection.cursor()
    cursor.execute(sql_select_Query)
    connection.commit()
while arg == True:
  FUNCTION =input ('Welcome to your SDP database to check Clients enter "check" ,to add new machines enter "add", to remove a client enter "rm" and type exit to end session: ')

  if FUNCTION== 'check':
      Check_DB()
  elif FUNCTION== 'add':
      ADD_MACHINE()
  elif FUNCTION== 'rm':
      REMOVE_MACHINE()
  elif FUNCTION == 'exit':
      arg = False
