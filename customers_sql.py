import pymysql

# Establish a connection to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='admin@123',
    database='mysql'
)
# insert data into customer table
# sql_command = "INSERT INTO customers (customer_id, name, age, num_purchases) VALUES (%s, %s, %s, %s)"
# data = [
#     (1, 'John Doe', 25, 3),
#     (2, 'Jane Smith', 30, 5),
#     (3, 'Mark Johnson', 35, 2),
# ]
# cursor = connection.cursor()

# for row in data:
#     cursor.execute(sql_command, row)

# connection.commit()

# cursor.close()
# connection.close()

# Retrieve all the customers from the "Customers" table whose age is greater than 25 and have made at least one purchase.

sql_command = "select * from customers where age>25 and num_purchases>=1"
cursor = connection.cursor()
cursor.execute(sql_command)
results = cursor.fetchall()
for row in results:
    print(row)





