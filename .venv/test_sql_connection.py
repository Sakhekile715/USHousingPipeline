import pyodbc
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get values from .env
driver = os.getenv("SQL_DRIVER")
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")

# Connection string
conn_str = f"""
    DRIVER={{{driver}}};
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


