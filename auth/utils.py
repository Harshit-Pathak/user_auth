from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "2c3ce214db26582209a8bb76e9f86533"   # generated using secrets library, secrets.token_hex(16)
ALGORITHM = "SH256"


def check_password(plain_password: str, hashed_password: str) -> bool:
    return PASSWORD_CONTEXT.verify(plain_password, hashed_password)


def generate_passwd_hash(plain_password: str) -> str:
    return PASSWORD_CONTEXT.hash(plain_password)


def create_access_token(data: dict, expires: timedelta | None = None):
    data = data.copy()
    now = datetime.now()
    if not expires:
        expires = timedelta(minutes=30)
    data.update({"exp": now + expires})
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return token


def decode_token(token: str) -> dict | None:
    try:
        data = jwt.decode(token, SECRET_KEY)
        return data
    except Exception:
        return {}


def get_user_from_jwt(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except jwt.PyJWTError:
        return None
    return username
