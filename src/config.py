import os
from dotenv import load_dotenv

load_dotenv()

API_URL=os.getenv("API_URL")
API_KEY=os.getenv("API_KEY")
DB_URL=os.getenv("DB_URL")

print(API_URL)
print(API_KEY)