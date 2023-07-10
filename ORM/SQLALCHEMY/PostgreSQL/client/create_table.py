from config.connection import base, engine
from database.models import Clients

table = Clients
base.metadata.create_all(engine)
