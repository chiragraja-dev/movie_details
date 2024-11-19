from app.db import get_db
# from app.models

def sample():
    db = get_db()
    return {"status":200, "message":"Candidate added successfully."}
