import pyodbc

# Use ODBC Driver 17 or 18 as installed
driver = '{ODBC Driver 17 for SQL Server}'
server = 'SAKHEKILE\SQLEXPRESS'
database = 'USHousingETL'

# Windows Authentication
conn_str = f"""
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    Trusted_Connection=yes;
"""

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT GETDATE();")
    result = cursor.fetchone()
    print("✅ SQL Server connected. Current server time:", result[0])
    conn.close()
except Exception as e:
    print("❌ Connection failed:", str(e))

