from fastapi import FastAPI
app = FastAPI()
#home page
@app.get("/")
def home():
    return {"x": 3, "y":4}