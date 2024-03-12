from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ziraat(Base):
    __tablename__ = 'ziraat'

    id = Column(Integer, primary_key=True)
    Date = Column(DateTime)
    Invoice_No = Column('Invoice No.', String)
    Explanation = Column(String)
    Transaction_Amount = Column('Transaction Amount', Integer)
    Balance = Column(Integer)

    def __init__(self, **kwargs):
        self.date = 'Date'
        self.invoice_no = 'invoice_no'
        self.explanation = 'explanation'
        self.transaction_amount = 'transaction_amount'
        self.balance = 'balance'
