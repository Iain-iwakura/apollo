import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from event_bot.models import Base

db_user = os.getenv('DB_USER', 'root')
db_pass = os.getenv('DB_PASS', '')

# Create database
os.system(f"mysql -u{db_user} -p{db_pass} -e 'create database event_bot';")

# Create tables
engine = create_engine(f'mysql://{db_user}:{db_pass}@localhost/event_bot')
Base.metadata.create_all(engine)