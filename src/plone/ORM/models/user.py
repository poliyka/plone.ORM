import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import enum

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3
    
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    fullname = sa.Column(sa.String)
    nickname = sa.Column(sa.String)
    
    # https://docs.sqlalchemy.org/en/13/core/type_basics.html
    BigInteger = sa.Column(sa.BigInteger)
    Boolean = sa.Column(sa.Boolean)
    Date = sa.Column(sa.Date)
    DateTime = sa.Column(sa.DateTime)
    Enum = sa.Column(sa.Enum(MyEnum))
    Float = sa.Column(sa.Float)
    Integer = sa.Column(sa.Integer)
    Interval = sa.Column(sa.Interval)
    LargeBinary = sa.Column(sa.LargeBinary)
    Numeric = sa.Column(sa.Numeric)
    PickleType = sa.Column(sa.PickleType)
    SmallInteger = sa.Column(sa.SmallInteger)
    String = sa.Column(sa.String)
    Text = sa.Column(sa.Text)
    Time = sa.Column(sa.Time)
    Unicode = sa.Column(sa.Unicode)
    UnicodeText = sa.Column(sa.UnicodeText)
    
    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"
