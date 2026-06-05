from sqlalchemy import create_engine
#SqlAlchemy is an Object Relational Mapper (ORM) that allows us to interact with databases using Python objects instead of writing raw SQL queries.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Udemy_python/Udemy_AIPractice/Backend_Python/todosapp.db"
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Manas6220@localhost/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Manas6220@127.0.0.1:3306/todoapplicationdatabase'
  
#Creates the connection to db or helps create db if no db:
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False}) #Now sqlite will allow more than one thread to cummunicate with it

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)#A session is like a temporary conversation/working area with the database.
#SessionLocal becomes a new session class configured with this engine

Base = declarative_base() #Creates table structure 






