
# AuthShield

Proyecto desarrollado para el Hackathon CIBERGU 2026.

## Descripción

AuthShield es un sistema de autenticación seguro diseñado para proteger aplicaciones web mediante el uso de tokens y control de acceso por roles.

El objetivo es aplicar buenas prácticas de ciberseguridad para evitar accesos no autorizados, proteger la identidad de los usuarios y prevenir vulnerabilidades comunes en sistemas de login.

## Problema que resuelve

Muchos sistemas de autenticación presentan debilidades que pueden permitir:

- Suplantación de identidad
- Elevación de privilegios
- Robo de credenciales
- Acceso no autorizado a información sensible

Este proyecto busca demostrar cómo implementar un sistema de autenticación siguiendo principios de seguridad desde el diseño.

## Funcionalidades principales

- Registro de usuarios
- Inicio de sesión seguro
- Generación de token de autenticación
- Acceso a rutas protegidas
- Control de roles (usuario / administrador)
- Protección básica frente a ataques comunes

## Tecnologías previstas

- Python
- FastAPI
- JWT (JSON Web Tokens)
- SQLite
- HTML / CSS / JavaScript

## Objetivo del proyecto

Diseñar una base sólida de autenticación segura que pueda ser ampliada en el futuro con:

- verificación en dos pasos (2FA)
- auditoría de accesos
- integración con sistemas cloud
