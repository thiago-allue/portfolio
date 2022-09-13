######################
#    Section 5 - AWS Relational Database Service (RDS)
#
#####################

### ./1.+CreateMInstance.py ####################################
import boto3
from pprint import pprint

rds_client = boto3.client('rds')

response = rds_client.create_db_instance(
    DBName="rdstuts",
    DBInstanceIdentifier="rdstuts",
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='MySQL',
    MasterUsername='admins',
    MasterUserPassword='password',
    Port=3306,
    EngineVersion='8.0.27',
    PubliclyAccessible=True,
    StorageType='gp2'
)

pprint(response)


### ./2.+CreateDatabase.py ####################################
import mysql.connector as mc

#dbtuts
try:
    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password"
    )

    dbname = input("Please enter your database name :")

    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE {} ".format(dbname))
    print("Database creatded ")

except mc.Error as e:
    print("Failed to create database {} ".format(e))


### ./3.+CheckCon.py ####################################
import mysql.connector as mc

try:
    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database="dbtuts"
    )

    print("Connection created")

except mc.Error as e:
    print("There is no connection {} ".format(e))


### ./4.+CreateTable.py ####################################
import mysql.connector as mc

try:
    mydb =mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database="dbtuts"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE Person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), lastname VARCHAR(255))")
    print("Table is created")

except mc.Error as e:
    print("Failed to create table {} ".format(e))


### ./5.+ShowTable.py ####################################
import mysql.connector as mc

try:
    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database="dbtuts"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for table in mycursor:
        print(table)

except mc.Error as e:
    print("Can not show the tables {} ".format(e))


### ./6.+InsertData.py ####################################
import mysql.connector as mc

try:
    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database="dbtuts"
    )

    mycursor = mydb.cursor()

    name = input("Please enter your name : ")
    lastname = input("Please enter your lastname : ")

    query = "INSERT INTO Person (name, lastname) VALUES (%s, %s)"
    value = (name,lastname)

    mycursor.execute(query, value)

    mydb.commit()
    print("Data Inserted")

except mc.Error as e:
    print("Failed to add data {} ".format(e))


### ./7.+ShowData.py ####################################
import mysql.connector as mc

try:
    dbname = input("Please enter the database name : ")
    tablename = input("Please enter the table name : ")

    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database=dbname
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM {} ".format(tablename))

    result = mycursor.fetchall()

    for data in result:
        print(data)

except mc.Error as e:
    print("Can not show the data ".format(e))


### ./8.+UpdateData.py ####################################
import mysql.connector as mc

try:
    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database="dbtuts"
    )

    mycursor = mydb.cursor()

    query = "UPDATE Person SET name='updated' WHERE id='1'"

    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record affected")

except mc.Error as e:
    print("Can not update data {} ".format(e))


### ./9.+DeleteData.py ####################################
import mysql.connector as mc

try:
    mydb = mc.connect(
        host="rdstuts.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database="dbtuts"
    )

    mycursor = mydb.cursor()

    query = "DELETE FROM Person WHERE id='1'"

    mycursor.execute(query)

    mydb.commit()

    print(mycursor.rowcount, "record affected")

except mc.Error as e:
    print("Can not delete the item {} ".format(e))

### ./10.+DecribeInfo.py ####################################
import boto3
from pprint import pprint

rds_client = boto3.client('rds')

response = rds_client.describe_db_instances(
    DBInstanceIdentifier = "rdstuts"
)

pprint(response)


### ./11.+DeleteMySQLInstance.py ####################################
import boto3

rds_client = boto3.client('rds')

response = rds_client.delete_db_instance(
    DBInstanceIdentifier="rdstuts",
    SkipFinalSnapshot=False,
    FinalDBSnapshotIdentifier="rdstuts-final-snapshot",
    DeleteAutomatedBackups=True

)
print(response)


### ./12.+CreatePostDb.py ####################################
import psycopg2

try:
    conn = psycopg2.connect(
        user="postgres",
        password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    conn.autocommit=True

    mycursor = conn.cursor()

    query = "CREATE DATABASE mydb"

    mycursor.execute(query)
    print("Database created")

except:
    print("Failed to create database")


### ./13.+CheckPostCon.py ####################################
import psycopg2

try:
    conn = psycopg2.connect(
        database="mydb",
        user="postgres",
        password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    print("Database connected")

except:
    print("Faild to connect the database")


### ./14.+CreateTable.py ####################################
import psycopg2

try:
    conn = psycopg2.connect(
        database="mydb", user="postgres", password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    cur = conn.cursor()
    query = "CREATE TABLE Employee (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL)"
    cur.execute(query)
    conn.commit()
    print("Table created")

except:
    print("Can not create table")


### ./15.+InsertData.py ####################################
import psycopg2

try:
    conn = psycopg2.connect(
        database="mydb", user="postgres", password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    cur = conn.cursor()

    query = "INSERT INTO Employee (ID, NAME, EMAIL) VALUES (1, 'parwiz', 'par@gmail.com')"
    cur.execute(query)
    conn.commit()
    print("Data has been added")

except:
    print("Can not add teh data")


### ./16.+SelectPostData.py ####################################
import psycopg2

try:
    conn = psycopg2.connect(
        database="mydb", user="postgres", password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    cur = conn.cursor()

    query = "SELECT * FROM Employee"

    cur.execute(query)

    rows = cur.fetchall()

    for data in rows:
        print("ID : " + str(data[0]))
        print("Name : " + data[1])
        print("Email : " + data[2])

except:
    print("Can not read the data")


### ./17.+UpdatePost.py ####################################
import psycopg2


try:
    conn = psycopg2.connect(
        database="mydb", user="postgres", password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    cur = conn.cursor()

    query = "UPDATE Employee SET EMAIL = 'updated@gmail.com' WHERE id=1"
    cur.execute(query)

    conn.commit()
    print("Data updated")
    print("Total Row Affected " + str(cur.rowcount))

except:
    print("Unable to update the data")


### ./18.+DeletePostData.py ####################################
import psycopg2

try:
    conn = psycopg2.connect(
        database="mydb", user="postgres", password="password",
        host="postgresdb.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        port=5432
    )

    cur = conn.cursor()

    query = "DELETE FROM Employee WHERE id=1"

    cur.execute(query)
    conn.commit()
    print("Data deleted")
    print("Total number of row deleted " + str(cur.rowcount))

except:
    print("Unable to delete the data")

### ./20.+CheckMariaCon.py ####################################
import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"

    )

    print("There is a connection with the database")

except mariadb.Error as e:
    print("There is not any connection {} ".format(e))


### ./21.+CreateMariaTable.py ####################################
import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"
    )

    cur = db.cursor()
    cur.execute("CREATE TABLE Person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),lastname VARCHAR(255) )")
    print("Table created ")

except mariadb.Error as e:
    print("Can not create table {} ".format(e))


### ./22.+ShowMariaTable.py ####################################
import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"
    )
    cur = db.cursor()

    cur.execute("SHOW TABLES")

    for data in cur:
        print(data)

except mariadb.Error as e:
    print("Can not show the table {} ".format(e))


### ./23.+InsertMariaData.py ####################################
import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"
    )

    cur = db.cursor()

    name = input("Please enter your name : ")
    lastname = input("Please enter your lastname : ")

    query = "INSERT INTO Person (name, lastname) VALUES (%s, %s)"

    value = (name, lastname)

    cur.execute(query, value)
    db.commit()

    print("Data inserted")

except mariadb.Error as e:
    print("Unable to insert data {} ".format(e))


### ./24.+GetMariaData.py ####################################
import mariadb

try:
    dbname = input("Please enter database name : ")
    tblname = input("Please enter table name : ")

    db = mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM {} ".format(tblname))

    result = cur.fetchall()

    for data in result:
        print(data)

except mariadb.Error as e:
    print("Unable to get the data {} ".format(e))


### ./25.+UpdateMariaData.py ####################################
import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"
    )
    cur = db.cursor()

    query = "UPDATE Person SET name = 'updatedname' WHERE id=3"

    cur.execute(query)

    db.commit()

    print(cur.rowcount, "record updated")

except mariadb.Error as e:
    print("Unable to update the data {} ".format(e))


### ./26.+DeleteMariaData.py ####################################
import mariadb

try:
    db=mariadb.connect(
        host="mariadbinstance.clrnsymfz2e0.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydbexample"
    )
    cur = db.cursor()

    query = "DELETE FROM Person WHERE id = 3"

    cur.execute(query)

    db.commit()

    print(cur.rowcount, "record deleted")

except mariadb.Error as e:
    print("Unable to delete the data {} ".format(e))


