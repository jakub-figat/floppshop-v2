from fastapi import HTTPException, status

auth_exception = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials.")
