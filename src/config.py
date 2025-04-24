import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("API_KEY")
DB_URL=os.getenv("DB_URL")
