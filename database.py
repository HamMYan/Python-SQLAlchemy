from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  


engine = create_engine("mysql+pymysql://root@localhost/python_mysql")

Session = sessionmaker(bind=engine)
session = Session()

try:
    connection = engine.connect()
    print("---------------MySQL connection successfuly created---------------")
    connection.close()
except Exception as err:
    print("Connection failed: ", err)

