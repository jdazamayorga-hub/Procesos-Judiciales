# config.py — Ajustes del monitor judicial

CORREO_ACTIVO = False
SMTP_SERVIDOR = "smtp.gmail.com"
SMTP_PUERTO = 587
CORREO_REMITENTE = "tucorreo@gmail.com"
CORREO_CLAVE_APP = "xxxx xxxx xxxx xxxx"
CORREO_DESTINO = "tucorreo@skandia.com.co"

CRITICIDAD_ALTA = [
    "sentencia", "revoca", "falla", "resuelve", "confirma",
    "niega", "concede", "condena", "absuelve", "declara probada",
    "declara no probada", "fallo", "termina"
]
CRITICIDAD_MEDIA = [
    "auto", "admite", "inadmite", "rechaza", "traslado",
    "requiere", "requerimiento", "notifica", "notificacion",
    "audiencia", "fija fecha", "corre traslado", "ordena"
]

TIMEOUT = 30
PAUSA_ENTRE_CONSULTAS = 3
REINTENTOS = 2
