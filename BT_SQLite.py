import sqlite3
import pandas as pd

def get_customers_with_min_invoices(database_path, min_invoices):
    """
    Trả về danh sách Customer có tham gia >= N hóa đơn (Invoice).

    Args:
        database_path (str): Đường dẫn tới file SQLite database.
        min_invoices (int): Số hóa đơn tối thiểu mà Customer tham gia.

    Returns:
        pd.DataFrame: DataFrame chứa danh sách các Customer thỏa mãn điều kiện.
    """
    sqliteConnection = None
    try:
        sqliteConnection = sqlite3.connect(database_path)
        cursor = sqliteConnection.cursor()
        print("Connected to the database")

        query = f"""
        SELECT Customer.CustomerId, Customer.FirstName, Customer.LastName, COUNT(Invoice.InvoiceId) AS InvoiceCount
        FROM Customer
        INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId
        HAVING InvoiceCount >= {min_invoices}
        """

        cursor.execute(query)
        columns = [column[0] for column in cursor.description]  # Lấy tên các cột
        result = pd.DataFrame(cursor.fetchall(), columns=columns)

        cursor.close()

        return result

    except sqlite3.Error as error:
        print("Error occurred - ", error)
        return None

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("SQLite Connection closed")


database_path = '../Databases/Chinook_Sqlite.sqlite'  # Đường dẫn đến tệp SQLite
min_invoices = int(input("Nhập số lượng hóa đơn tối thiểu (N): "))

customers = get_customers_with_min_invoices(database_path, min_invoices)
if customers is not None and not customers.empty:
    print(f"\nDanh sách Customer có tham gia >= {min_invoices} hóa đơn:")
    print(customers)
else:
    print(f"\nKhông có Customer nào tham gia >= {min_invoices} hóa đơn.")
