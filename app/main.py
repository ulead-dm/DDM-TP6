from fastapi import FastAPI, HTTPException

from app.model import load_model, predict
from app.schemas import PredictRequest, PredictResponse, HealthResponse

app = FastAPI(
    title='TP6 API',
    description='API de predicción con un modelo sklearn',
    version='1.0.0',
)


@app.on_event('startup')
def startup_event():
    try:
        load_model()
    except Exception as exc:
        raise RuntimeError(f'No se pudo cargar el modelo al iniciar: {exc}')


@app.get('/health', response_model=HealthResponse)
def health():
    return {
        'status': 'healthy',
        'model_loaded': True,
        'model_version': '1.0',
    }


@app.post('/predict', response_model=PredictResponse)
def predict_endpoint(payload: PredictRequest):
    try:
        result = predict([
            payload.feature_1,
            payload.feature_2,
            payload.feature_3,
        ])

        return PredictResponse(
            label=result['label'],
            probability=result['probability'],
            model_version=result['model_version'],
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f'Error de inferencia: {exc}')
