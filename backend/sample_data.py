from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["emailApp"]
coll = db["orders"]
coll.delete_many({})  

customers = [
    {
        "customerId": "C001",
        "name": "Alice",
        "email": "alice@example.com",
        "orders": [
            {"orderId": "O001", "amount": 800, "category": "Books", "date": "2024-10-01"},
            {"orderId": "O002", "amount": 1500, "category": "Electronics", "date": "2025-03-20"},
            {"orderId": "O003", "amount": 900, "category": "Books", "date": "2025-04-01"},
        ]
    },
    {
        "customerId": "C002",
        "name": "Bob",
        "email": "bob@example.com",
        "orders": [
            {"orderId": "O004", "amount": 450, "category": "Clothing", "date": "2024-05-10"},
        ]
    },
    {
        "customerId": "C003",
        "name": "Charlie",
        "email": "charlie@example.com",
        "orders": [
            {"orderId": "O005", "amount": 300, "category": "Books", "date": "2024-06-20"},
            {"orderId": "O006", "amount": 250, "category": "Books", "date": "2024-07-10"},
        ]
    },
    {
        "customerId": "C004",
        "name": "Diana",
        "email": "diana@example.com",
        "orders": [
            {"orderId": "O007", "amount": 2000, "category": "Electronics", "date": "2025-02-10"},
            {"orderId": "O008", "amount": 1500, "category": "Electronics", "date": "2025-04-01"},
        ]
    },
    {
        "customerId": "C005",
        "name": "Ethan",
        "email": "ethan@example.com",
        "orders": [
            {"orderId": "O009", "amount": 300, "category": "Clothing", "date": "2025-01-01"},
        ]
    },
    {
        "customerId": "C006",
        "name": "Fiona",
        "email": "fiona@example.com",
        "orders": [
            {"orderId": "O010", "amount": 500, "category": "Books", "date": "2024-12-10"},
            {"orderId": "O011", "amount": 600, "category": "Clothing", "date": "2025-01-25"},
            {"orderId": "O012", "amount": 700, "category": "Clothing", "date": "2025-02-14"},
        ]
    },
    {
        "customerId": "C007",
        "name": "George",
        "email": "george@example.com",
        "orders": [
            {"orderId": "O013", "amount": 1000, "category": "Books", "date": "2024-11-11"},
            {"orderId": "O014", "amount": 500, "category": "Electronics", "date": "2025-03-15"},
        ]
    },
    {
        "customerId": "C008",
        "name": "Hannah",
        "email": "hannah@example.com",
        "orders": [
            {"orderId": "O015", "amount": 200, "category": "Books", "date": "2024-04-22"},
            {"orderId": "O016", "amount": 250, "category": "Clothing", "date": "2024-05-05"},
        ]
    }
]

coll.insert_many(customers)
print("Sample data inserted.")
