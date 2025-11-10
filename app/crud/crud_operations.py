from app.database.mongo_client import db
from app.utils.serializers import serialize_doc, serialize_docs
from bson import ObjectId

# -------------------------------
# Generic CRUD functions
# -------------------------------

def create_document(collection: str, data: dict):
    result = db[collection].insert_one(data)
    return serialize_doc(db[collection].find_one({"_id": result.inserted_id}))

def get_all_documents(collection: str):
    return serialize_docs(db[collection].find())

def get_document_by_id(collection: str, id: str):
    return serialize_doc(db[collection].find_one({"_id": ObjectId(id)}))

def update_document(collection: str, id: str, data: dict):
    db[collection].update_one({"_id": ObjectId(id)}, {"$set": data})
    return serialize_doc(db[collection].find_one({"_id": ObjectId(id)}))

def delete_document(collection: str, id: str):
    db[collection].delete_one({"_id": ObjectId(id)})
    return {"message": f"Documento eliminado de {collection}"}

def get_document_by_field(collection_name, field, value):
    collection = db[collection_name]
    return serialize_doc(collection.find_one({field: value}))