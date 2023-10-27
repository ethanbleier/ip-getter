import requests
import mysql.connector

# template code
# mysql -h sql3.freemysqlhosting.net -P 3306 -u sql3655032 -p
# password
# kPzxfFuz7q

conn = {
    "user": "sql3655032",
    "password": "kPzxfFuz7q",
    "host": "sql3.freemysqlhosting.net",
    "database": "sql3655032",  
}

try:

    ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
    print(ip)

    connection = mysql.connector.connect(**conn)
    c = connection.cursor()
    stored_ip = c.fetchone()
    print(stored_ip)
    if ip != stored_ip:
        insert = "UPDATE `info`\nSELECT * FROM `info`\nSET 1 = %s", ip
        c.execute(insert, ip)
        connection.commit()
        print("**** New IP Found ****\n\tAdding to database\t")
    else:
        print("**** New IP identical to database IP ****\n\tDoing nothing\t")
except Exception as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        c.close()
        connection.close()
