from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

app = FastAPI(title="AuthShield API")

SECRET_KEY = "authshield_clave_secreta"
ALGORITHM = "HS256"


@app.get("/")
def home():
    return {"message": "AuthShield API funcionando correctamente"}


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# Base de datos simulada
fake_user_db = {}


@app.post("/register")
def register(user: UserRegister):
    hashed_password = pbkdf2_sha256.hash(user.password)

    fake_user_db[user.username] = {
        "username": user.username,
        "hashed_password": hashed_password
    }

    return {
        "message": "Usuario registrado correctamente",
        "username": user.username,
        "hashed_password": hashed_password
    }


@app.post("/login")
def login(user: UserLogin):
    db_user = fake_user_db.get(user.username)

    if not db_user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not pbkdf2_sha256.verify(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    # TOKEN CON EXPIRACIÓN (2 minutos)
    expire = datetime.now(timezone.utc) + timedelta(minutes=2)

    token_data = {
        "sub": user.username,
        "exp": expire
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "message": "Login correcto",
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/profile")
def profile(token: str = Header(None)):
    if not token:
        raise HTTPException(status_code=401, detail="Token no proporcionado")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if not username:
            raise HTTPException(status_code=401, detail="Token inválido")

        return {
            "message": "Acceso autorizado al perfil",
            "username": username
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")