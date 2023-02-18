from fastapi import FastAPI

app = FastAPI(
    title="Poet",
    description="A sorta social media site",
)

from .auth.routes import router as auth_router

app.include_router(auth_router, prefix="/auth")


@app.get("/ping")
async def ping() -> dict[str, str]:
    return {"message": "pong!"}
