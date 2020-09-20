import os

from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, ARRAY

# DATABASE_URL = "postgresql://postgres:Pass2020!@localhost/movie_db"
DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)

metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("plot", String(250)),
    Column("genres", ARRAY(String)),
    Column("casts_id", ARRAY(Integer)),
)
# movies.create(engine)
database = Database(DATABASE_URI)
