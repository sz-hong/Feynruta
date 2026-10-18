from fastapi import FastAPI
from auth.router import router as auth_router
from realtime.ws import router as ws_router

app = FastAPI()
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(ws_router)
#home page
@app.get("/users/{user_id}")
async def home(user_id: int):
    return f"{user_id}"