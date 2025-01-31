from motor.motor_asyncio import AsyncIOMotorClient

#MONGO_URI = "mongodb://datacenter:27017"
#MONGO_URI = "mongodb://localhost:27017"   
MONGO_URI = "mongodb://mongodb:27017"

DB_NAME = "auth_service"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
