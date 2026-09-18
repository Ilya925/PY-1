from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"first_response": "Test Get request"}

@app.get("/items/{item_id}")
def read_text(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

