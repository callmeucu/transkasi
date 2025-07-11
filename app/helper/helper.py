from passlib.context import CryptContext
import psycopg2
import os
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

# password hassing
pwd_context = CryptContext (schemes=["bcrypt"], deprecated="auto")

#mengatur agar password tidak terbaca didatabase.. hash md5
def hash_password(password : str) -> str:
    return pwd_context.hash(password)

#verifikasi password ketika login
def verify_password(plain_password : str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

#koneksi sementara backend dan database
def get_pg_connection ():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)
    return conn
