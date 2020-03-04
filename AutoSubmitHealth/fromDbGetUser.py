from db import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

content = create_engine('mysql+pymysql://root:root@localhost:3306/autosubmit')
Session = sessionmaker(bind=content)
session = Session()


def getUserAll():
    dict = []
    res = session.query(User).all()
    for i in res:
        dict.append({
            'username' : i.username,
            'password' : i.password,
            'site' : i.site,
            'phone' : i.phone
        })
    return dict