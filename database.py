import sqlite3
from datetime import datetime

# Create or connect to SQLite database
conn = sqlite3.connect("traffic.db", check_same_thread=False)
cursor = conn.cursor()

# Create table to store packet data
cursor.execute("""
CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_ip TEXT,
    dst_ip TEXT,
    protocol TEXT,
    length INTEGER,
    timestamp TEXT
)
""")
conn.commit()

# Function to save packet info
def save_packet(src, dst, proto, length):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO packets (src_ip, dst_ip, protocol, length, timestamp) VALUES (?, ?, ?, ?, ?)",
                   (src, dst, str(proto), length, time_now))
    conn.commit()
