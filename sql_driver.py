import requests
from datetime import date
import mysql.connector

# template code
# mysql -h sql3.freemysqlhosting.net -P 3306 -u sql3657235 -p
# password
# kPzxfFuz7q

#New db username/name:
# sql3657235
# sj1dv4Wgvb

conn = {
    # "user": "root",
    "user": "sql3657235",
    "password": "sj1dv4Wgvb",
    # "password": "MyNewPass",
    "host": "sql3.freemysqlhosting.net",
    "database": "sql3657235",
    # "host": "localhost",
    "port": "3306"  
}

connection = None

try:
    ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
    print(ip)

    connection = mysql.connector.connect(**conn)
    c = connection.cursor()
    # stored_ip = c.fetchone()
    # print(stored_ip)
    # if ip != stored_ip:
    insert = "INSERT INTO info (data, createtime) VALUES (%s, %s) "
    result = c.execute(insert, (ip, date.today()))
    # print("result: ", result.rowcount)
    connection.commit()
    print("**** New IP Found ****\n\tAdding to database\t")
    # else:
        # print("**** New IP identical to database IP ****\n\tDoing nothing\t")
except Exception as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        c.close()
        connection.close()
