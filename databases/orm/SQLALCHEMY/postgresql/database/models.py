from config.connection import base
from config.libs import Column, Integer, String
 

# Section 1: Create SQL table
class Clients(base):
    __tablename__ = 'Clients'
    ID          = Column(Integer, primary_key=True)
    FirstName   = Column(String)
    LastName    = Column(String)
    Balance     = Column(Integer)
    Birthday    = Column(String)
    Email       = Column(String)

