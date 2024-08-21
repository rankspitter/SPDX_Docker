import mysql.connector
import os

# for windows host = 'localhost'
def ConnectorMysql():
    mydb = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        auth_plugin='mysql_native_password'
    )
    return mydb

def get_all():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT name FROM users "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    arr = []
    for result in myresult:
        arr.append(result[0])
    return arr


def get_data(_uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE uid = %s"
    mycursor.execute(sql, (_uid,))
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        for result in myresult:
            arr = {
                "uid"  : result[0],
                "name" : result[1],
                "age"  : int(result[2])
            }
    return arr


def insert_data(uid, name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (uid, name, age) VALUES (%s, %s, %s)"
    val = (uid, name, age)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

def update_date(uid, name, age): 
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "UPDATE users SET uid=%s, name=%s, age=%s WHERE uid=%s"
    val = (uid, name ,age, uid)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

def delete_date(uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = 'DELETE FROM users WHERE uid={}'.format(uid)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()




