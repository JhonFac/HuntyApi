from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:123@localhost:5432/python_db"
DATABASE_URL = "postgresql://postgres:J9Et6Aml3yNB0e4e4xt4@containers-us-west-163.railway.app:7547/railway"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
