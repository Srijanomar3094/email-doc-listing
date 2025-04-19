from fastapi import APIRouter
from pymongo import MongoClient
from datetime import datetime, timedelta

router = APIRouter()
client = MongoClient("mongodb://localhost:27017")
db = client["emailApp"]
orders = db["orders"]

@router.get("/customer-report")
def customer_report():
    six_months_ago = datetime.now() - timedelta(days=180)
    pipeline = [
        {"$unwind": "$orders"},
        {"$addFields": {
            "orders.date": {"$toDate": "$orders.date"}
        }},
        {"$group": {
            "_id": "$customerId",
            "name": {"$first": "$name"},
            "email": {"$first": "$email"},
            "totalSpent": {"$sum": "$orders.amount"},
            "averageOrderValue": {"$avg": "$orders.amount"},
            "lastPurchaseDate": {"$max": "$orders.date"},
            "orders": {"$push": "$orders"},
            "categoryWiseSpend": {"$push": {"k": "$orders.category", "v": "$orders.amount"}}
        }},
        {"$match": {"totalSpent": {"$gte": 500}}},
        {"$addFields": {
            "loyaltyTier": {
                "$switch": {
                    "branches": [
                        {"case": {"$lt": ["$totalSpent", 1000]}, "then": "Bronze"},
                        {"case": {"$and": [{"$gte": ["$totalSpent", 1000]}, {"$lte": ["$totalSpent", 3000]}]}, "then": "Silver"},
                        {"case": {"$gt": ["$totalSpent", 3000]}, "then": "Gold"}
                    ],
                    "default": "Bronze"
                }
            },
            "isActive": {"$gte": ["$lastPurchaseDate", six_months_ago]},
        }}
    ]
    result = list(orders.aggregate(pipeline))
    

    for customer in result:
        freq = {}
        for o in customer["orders"]:
            cat = o["category"]
            freq[cat] = freq.get(cat, 0) + 1
        favorite = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[0][0]
        customer["favoriteCategory"] = favorite

    
        cat_spend = {}
        for kv in customer["categoryWiseSpend"]:
            cat_spend[kv["k"]] = cat_spend.get(kv["k"], 0) + kv["v"]
        customer["categoryWiseSpend"] = cat_spend

    
        del customer["orders"]

    return result
