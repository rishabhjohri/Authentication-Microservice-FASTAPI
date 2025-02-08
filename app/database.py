from motor.motor_asyncio import AsyncIOMotorClient

#MONGO_URI = "mongodb://datacenter:27017"
#MONGO_URI = "mongodb://localhost:27017"   
#MONGO_URI = "mongodb://mongodb:27017"
MONGO_URI = "mongodb://admin:adminpass@192.168.56.107:27017/auth_service?authSource=admin"
DB_NAME = "auth_service"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]
