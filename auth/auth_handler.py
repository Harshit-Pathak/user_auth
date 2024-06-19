from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from .utils import decode_token


class JWTBearer(HTTPBearer):
    
    def verify_jwt(self, token: str) -> bool:
        try:
            data = decode_token(token)
            return data is not None
        except Exception:
            return False


security = JWTBearer()
