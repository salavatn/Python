from config.connection import session
from database.models import Clients


query = session.query(Clients)

for record in query:
    raw = {
        'ID':        record.ID,
        'FirstName': record.FirstName,
        'LastName':  record.LastName,
        'Balance':   record.Balance,
        'Birthday':  record.Birthday,
        'Email':     record.Email
    }
    print(raw)
