from fastapi import FastAPI, HTTPException
from bson import ObjectId
from app.database.mongo_client import collection
from app.models.models import Item, ItemUpdate

app = FastAPI(title="FastAPI + MongoDB CRUD")

# Helper to convert MongoDB _id to string
def serialize_item(item):
    item["_id"] = str(item["_id"])
    return item

@app.post("/items")
def create_item(item: Item):
    """Create a new item"""
    result = collection.insert_one(item.dict())
    new_item = collection.find_one({"_id": result.inserted_id})
    return serialize_item(new_item)

@app.get("/items")
def get_items():
    """Get all items"""
    items = [serialize_item(i) for i in collection.find()]
    return items

@app.get("/items/{item_id}")
def get_item(item_id: str):
    """Get one item by ID"""
    item = collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return serialize_item(item)

@app.put("/items/{item_id}")
def update_item(item_id: str, item: ItemUpdate):
    """Update item by ID"""
    update_data = {k: v for k, v in item.dict().items() if v is not None}
    updated = collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": update_data}
    )
    if updated.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = collection.find_one({"_id": ObjectId(item_id)})
    return serialize_item(updated_item)

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    """Delete item by ID"""
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
