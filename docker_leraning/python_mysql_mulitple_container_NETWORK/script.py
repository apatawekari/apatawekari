import mysql.connector
from mysql.connector import Error

def insert_user_data(name, age, gender,connection): 
    try:
        """ Insert user data into MySQL database table """ 
        if connection.is_connected(): 
            cursor = connection.cursor() 
            insert_query = """INSERT INTO user_entry (name, age, gender) VALUES (%s, %s, %s )""" 
            data_tuple = (name, age, gender) 
            cursor.execute(insert_query, data_tuple) 
            connection.commit() 
            print("Record inserted successfully") 
    except Error as e:        
        print("Failed to insert record into MySQL table")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
def connect():
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(
            host='mysql-container',    # use other container name after creating using same network 
            database='testdb',
            user='admin',
            password='root'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            
            cursor.execute("CREATE TABLE IF NOT EXISTS user_entry (" "id INT AUTO_INCREMENT PRIMARY KEY, " "name VARCHAR(255) NOT NULL, " "age INT, " "gender ENUM('Male', 'Female') " ")")
            name = input("Enter your name: ") 
            age = int(input("Enter your age: ")) 
            gender = input("Enter your gender (Male/Female): ") 
            insert_user_data(name, age, gender,connection)
    except Error as e:
        print("Error while connecting to MySQL", e)



if __name__ == '__main__':
    connect()





# pip install mysql-connector-python
