# Libs 1: sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Libs 2: sqlalchemy models
from sqlalchemy import Column, Integer, String

from dotenv import load_dotenv
from faker import Faker
import os
