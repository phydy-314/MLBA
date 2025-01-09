import sqlite3
import pandas as pd

sqliteConnection = None  # Khởi tạo biến trước khối try
try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('../Database/Chinook_Sqlite.sqlite')  # Đảm bảo đường dẫn đúng
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Write a query and execute it with cursor
    query = 'SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)

    # Fetch and output result
    df = pd.DataFrame(cursor.fetchall())
    print(df)

    # Close the cursor
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred - ', error)

finally:
    # Close DB Connection irrespective of success or failure
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
