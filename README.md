```
████████╗██████╗  ██████╗        ██████╗ ██████╗ ███╗   ███╗
╚══██╔══╝██╔══██╗██╔════╝        ██╔══██╗██╔══██╗████╗ ████║
   ██║   ██████╔╝███████╗  █████╗██║  ██║██║  ██║██╔████╔██║
   ██║   ██╔═══╝ ██╔══██║  ╚════╝██║  ██║██║  ██║██║╚██╔╝██║
   ██║   ██║     ███████║        ██████╔╝██████╔╝██║ ╚═╝ ██║
   ╚═╝   ╚═╝     ╚══════╝        ╚═════╝ ╚═════╝ ╚═╝     ╚═╝

        FastAPI + Scikit-Learn Model Deployment
```

# TP6 – API de Machine Learning

API REST desarrollada con **FastAPI** para servir un **modelo de clasificación entrenado con scikit-learn**.

El objetivo del proyecto es demostrar un **flujo completo de despliegue de modelos**:

- entrenamiento del modelo  
- serialización con `joblib`  
- exposición mediante API  
- contenedorización con Docker  

---

# Arquitectura del Proyecto

```
trabajo_practico_6_diegodm/
│
├── app/
│   ├── main.py        # FastAPI app y endpoints
│   ├── model.py       # Carga del modelo y lógica de predicción
│   └── schemas.py     # Validación de datos con Pydantic
│
├── models/
│   ├── final_meta_classifier.joblib
│   └── ...
│
├── Dockerfile         # Imagen para despliegue
├── requirements.txt   # Dependencias Python
└── README.md
```

---

# Requisitos

- Python **3.10+**
- pip
- Docker *(opcional para despliegue)*

---

# Instalación de dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar la API localmente

```bash
uvicorn app.main:app --reload --port 8000
```

La API quedará disponible en:

```
http://127.0.0.1:8000
```

Documentación automática:

```
http://127.0.0.1:8000/docs
```

FastAPI genera automáticamente **Swagger UI** para probar los endpoints.

---

# Endpoints disponibles

## Health Check

```
GET /health
```

Verifica el estado del servicio y si el modelo está cargado.

Ejemplo de respuesta:

```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "1.0"
}
```

---

## Predicción

```
POST /predict
```

Request:

```json
{
  "feature_1": 1.0,
  "feature_2": 2.0,
  "feature_3": 3.0
}
```

Response:

```json
{
  "label": 1,
  "probability": 0.999,
  "model_version": "1.0"
}
```

---

# Docker

## Construir la imagen

```bash
docker build -t <usuario>/tp6-api:1.0 .
```

---

## Ejecutar contenedor

```bash
docker run --rm -p 8000:8000 <usuario>/tp6-api:1.0
```

---

## Verificar funcionamiento

```bash
curl http://127.0.0.1:8000/health
```

---

# Publicar en Docker Hub

Login:

```bash
docker login
```

Subir imagen:

```bash
docker push <usuario>/tp6-api:1.0
```

---

# Notas técnicas

- El modelo **se carga una única vez al iniciar la aplicación** para evitar latencias.
- La validación de datos se realiza con **Pydantic** (`app/schemas.py`).
- Si se modifican los **features del modelo**, se deben actualizar:

```
app/schemas.py
app/main.py
```

---

# Tecnologías utilizadas

- FastAPI
- Scikit-Learn
- Pydantic
- Uvicorn
- Docker
- Joblib

