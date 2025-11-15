from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Shreyas%40123@localhost:5432/smartcity"
)
connection = engine.connect()
print("✅ Connected successfully!")