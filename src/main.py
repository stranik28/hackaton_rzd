from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from database import create_tables
from transport_routing.router import router as transport_routing_router
from predict.router import router as predict_router
from admin_data.router import router as admin_router

app = FastAPI(
    title = "RZD"
)

@app.on_event("startup")
async def startup():
    await create_tables()
    redis = aioredis.from_url("redis://redis:6379")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

app.include_router(transport_routing_router)
app.include_router(predict_router)
app.include_router(admin_router)