from db import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

content = create_engine('mysql+pymysql://root:root@localhost:3306/autosubmit')
Session = sessionmaker(bind=content)
session = Session()

def addUser(userDict:dict):
    obj = User(username=userDict['username'], password=userDict['password'], site=userDict['site'], phone=userDict['phone'])
    session.add(obj)
    session.commit()