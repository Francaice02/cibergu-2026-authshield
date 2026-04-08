# AuthShield API 🔐

AuthShield es una API segura desarrollada con FastAPI que implementa autenticación basada en JWT (JSON Web Tokens).

El proyecto demuestra cómo proteger endpoints mediante tokens seguros, aplicar hashing de contraseñas y limitar el acceso a recursos sensibles.

Este tipo de arquitectura es común en entornos Cloud, microservicios y aplicaciones empresariales.

---

## Tecnologías utilizadas

- Python
- FastAPI
- JWT (JSON Web Token)
- Passlib (hash seguro de contraseñas)
- Uvicorn
- Swagger UI

---

## Funcionalidades implementadas

### Registro de usuario
Permite crear nuevos usuarios almacenando la contraseña de forma segura mediante hashing.

Endpoint:

POST /register

---

### Login seguro
Valida las credenciales del usuario y genera un token JWT.

Endpoint:

POST /login

---

### Token JWT con expiración
El sistema genera tokens con expiración de 15 minutos, reduciendo riesgos de seguridad.

---

### Endpoint protegido
Solo los usuarios con token válido pueden acceder al perfil.

Endpoint:

GET /profile

Requiere header:

token: JWT_TOKEN

---

## Flujo de autenticación

1. El usuario se registra
2. El usuario inicia sesión
3. El sistema genera un token JWT
4. El token se envía en cada petición protegida
5. El sistema valida el token antes de permitir acceso

---

## Cómo ejecutar el proyecto

Instalar dependencias:

pip install fastapi uvicorn python-jose passlib

Ejecutar servidor:

uvicorn main:app --reload

Abrir documentación automática:

http://127.0.0.1:8000/docs

---

## Conceptos de seguridad aplicados

- Hash seguro de contraseñas
- Autenticación basada en tokens
- Control de acceso a endpoints
- Expiración de credenciales
- Protección de información sensible

---

## Autor

Proyecto desarrollado como práctica de seguridad backend enfocada a Cloud Security.
