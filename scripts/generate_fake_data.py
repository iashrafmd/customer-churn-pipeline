import psycopg2
from faker import Faker
import uuid
import random

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    dbname="churn_db",          
    user="postgres",            
    password="Aashu@99", 
    port=5432
)

cur = conn.cursor()

def insert_customers(n=1000):
    for _ in range(n):
        cid = str(uuid.uuid4())
        name = fake.name()
        email = fake.email()
        signup_date = fake.date_between(start_date='-2y', end_date='today')
        country = fake.country()
        is_active = random.choice([True, False])
        cur.execute(
            "INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s)",
            (cid, name, email, signup_date, country, is_active)
        )
    print(f"Inserted {n} customers.")

def insert_orders():
    cur.execute("SELECT customer_id, signup_date FROM customers")
    customers = cur.fetchall()

    for customer_id, signup_date in customers:
        num_orders = random.randint(2, 5)
        for _ in range(num_orders):
            order_id = str(uuid.uuid4())
            order_date = fake.date_between(start_date=signup_date, end_date="today")
            amount = round(random.uniform(20.0, 1000.0), 2)
            status = random.choice(['delivered', 'cancelled', 'returned'])

            cur.execute(
                "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                (order_id, customer_id, order_date, amount, status)
            )
    print("Orders inserted.")

def insert_payments():
    cur.execute("SELECT order_id, order_date FROM orders")
    orders = cur.fetchall()
    for order_id, order_date in orders:
        payment_id = str(uuid.uuid4())
        payment_date = fake.date_between(start_date=order_date, end_date="today")
        method = random.choice(['card', 'cash on delivery', 'paypal'])
        success = random.choices([True, False], weights=[90, 10])[0]

        cur.execute(
            "INSERT INTO payments VALUES (%s, %s, %s, %s, %s)",
            (payment_id, order_id, payment_date, method, success)
        )
    print("Payments inserted.")

def insert_support_tickets():
    cur.execute("SELECT customer_id FROM customers")
    customers = cur.fetchall()

    for (customer_id,) in customers:
        if random.random() < 0.3:
            num_tickets = random.randint(1, 3)
            for _ in range(num_tickets):
                ticket_id = str(uuid.uuid4())
                created_at = fake.date_time_between(start_date='-1y', end_date='now')
                issue_type = random.choice(['late delivery', 'refund', 'login issue', 'payment failure', 'damaged item'])
                resolved = random.choices([True, False], weights=[80, 20])[0] 

                cur.execute(
                    "INSERT INTO support_tickets VALUES (%s, %s, %s, %s, %s)",
                    (ticket_id, customer_id, created_at, issue_type, resolved)
                )
    print("Support tickets inserted.")

insert_customers()
insert_orders()
insert_payments()
insert_support_tickets()
conn.commit()
cur.close()
conn.close()
print("Done inserting fake data.")
