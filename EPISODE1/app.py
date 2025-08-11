from sqlalchemy import create_engine , Column , Integer , String 
from sqlalchemy.orm import declarative_base

# dialect+driver://username:password@host:port/database
db_url = "sqlite:///mydatabase.db"

# "sqlite:////absolute/path/to/mydatabase.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key= True )
    name = Column(String)
    age = Column(Integer)


# Base.metadata.drop_all(engine)  
Base.metadata.create_all(engine)
print("DB create successfully")


# Format: dialect+driver://username:password@host:port/database

# Example 1: SQLite (local file)
# engine_sqlite = create_engine(
#     "sqlite:///mydatabase.db"   # sqlite:/// → relative path; sqlite://// → absolute path
# )

# # Example 2: PostgreSQL
# engine_postgres = create_engine(
#     "postgresql+psycopg2://user:password@localhost:5432/mydatabase"
#     # postgresql+psycopg2 → dialect+driver
#     # user:password       → database credentials
#     # localhost           → host where DB runs
#     # 5432                → default PostgreSQL port
#     # mydatabase          → database name
# )

# # Example 3: MySQL
# engine_mysql = create_engine(
#     "mysql+pymysql://user:password@localhost:3306/mydatabase"
#     # mysql+pymysql       → dialect+driver
#     # 3306                → default MySQL port
# )

# # Example 4: SQL Server
# engine_mssql = create_engine(
#     "mssql+pyodbc://user:password@myserver/mydatabase?driver=ODBC+Driver+17+for+SQL+Server"
#     # mssql+pyodbc        → dialect+driver
#     # ?driver=...         → specifies the ODBC driver
# )

# print("Engines created successfully!")

