from fastapi import FastAPI

from .api.db import database, metadata, engine
from .api.movies import movies

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies, prefix="/api/v1/movies", tags=["movies"])
