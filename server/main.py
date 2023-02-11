from fastapi import FastAPI

from .auth.routes import router as auth_router

app = FastAPI(
    title="Poet",
    description="A sorta social media site",
)

app.include_router(auth_router, prefix="/auth")


@app.get("/ping")
async def ping():
    return {"message": "pong!"}
