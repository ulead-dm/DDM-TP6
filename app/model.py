import os
from typing import List, Dict, Any

import joblib
import numpy as np

MODEL_VERSION = '1.0'
MODEL_FILENAME = 'final_meta_classifier.joblib'
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', MODEL_FILENAME)

_model = None


def load_model() -> Any:
    global _model
    if _model is not None:
        return _model

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f'Modelo no encontrado en {MODEL_PATH}')

    _model = joblib.load(MODEL_PATH)
    return _model


def predict(features: List[float]) -> Dict[str, Any]:
    model = load_model()
    x = np.asarray(features, dtype=float).reshape(1, -1)

    expected = getattr(model, 'n_features_in_', None)
    if expected is not None and x.shape[1] != expected:
        raise ValueError(f'Se esperaban {expected} valores (features), se recibieron {x.shape[1]}')

    try:
        prediction = model.predict(x)[0]
    except Exception as e:
        raise ValueError(f'Error al predecir: {e}')

    probability = None
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(x)
        if proba.shape[1] >= 2:
            probability = float(proba[0, 1])
        else:
            probability = float(proba[0, 0])

    return {
        'label': int(prediction),
        'probability': probability,
        'model_version': MODEL_VERSION,
    }
