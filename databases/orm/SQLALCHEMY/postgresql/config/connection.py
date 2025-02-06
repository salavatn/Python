from config.libs import create_engine, declarative_base, sessionmaker
from config.libs import load_dotenv, os


# Section 1: Load environment variables
load_dotenv()
user = os.environ['SUPABASE_USER']
pswd = os.environ['SUPABASE_PASSWD']
host = os.environ['SUPABASE_HOST']
port = os.environ['SUPABASE_PORT']
name = os.environ['SUPABASE_DB']


# Section 2: Create SQL connection
engine = create_engine(f'postgresql://{user}:{pswd}@{host}:{port}/{name}', echo=True)
base   = declarative_base()
session_maker = sessionmaker(bind=engine)
session       = session_maker()
