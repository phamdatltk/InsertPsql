import psycopg2
import time
import random
from datetime import datetime

# Kết nối tới cơ sở dữ liệu PostgreSQL
conn = psycopg2.connect(
    host="localhost",    
    database="test_database", 
    user="admin",        
    password="phamdat280102",
    port=5432
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    city VARCHAR(255),
    id SERIAL PRIMARY KEY,
    time TIMESTAMPTZ,
    status BOOLEAN
)
""")
conn.commit()

def insert_random_data():
    listCity = ["Hanoi", "SaiGon", "ThanhHoa", "CanTho", "NgheAn","KhanhHoa"]
    city = random.choice(listCity)
    time = datetime.now().isoformat()
    status = random.choice([True, False])
    
    query = "INSERT INTO data (city, time, status) VALUES (%s, %s, %s)"
    values = (city, time, status)
    cursor.execute(query, values)
    conn.commit()
    print(f"Inserted: {values}")


while True:
   insert_random_data()
   time.sleep(3)

