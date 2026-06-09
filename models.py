from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from database import Base

class Budget(Base):

    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)

    department = Column(String)

    category = Column(String)

    allocated_amount = Column(Float)

    spent_amount = Column(Float)

class Equipment(Base):

    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)

    item_name = Column(String)

    quantity = Column(Integer)

    location = Column(String)

class FundingRequest(Base):

    __tablename__ = "funding_requests"

    id = Column(Integer, primary_key=True)

    faculty_name = Column(String)

    purpose = Column(String)

    amount = Column(Float)

    status = Column(String)
