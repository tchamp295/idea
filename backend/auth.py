from fastapi import Depends, HTTPException

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

def authenticate(username: str, password: str):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    raise HTTPException(status_code=401, detail="Invalid credentials")
