from database.mysql_connection import engine

try:
    connection = engine.connect()

    print("MySQL Connection Successful")

    connection.close()

except Exception as e:
    print(f"Connection Failed: {e}")