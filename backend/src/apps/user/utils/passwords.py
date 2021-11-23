from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
