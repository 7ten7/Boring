from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String


class User(declarative_base()):
    __tablename__ = "User"
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    username = Column(String(11), primary_key=True)
    password = Column(String(20))
    site = Column(String(100))
    phone = Column(String(11))
