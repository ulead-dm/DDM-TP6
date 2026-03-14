from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    feature_1: float = Field(..., description='Feature numeric 1')
    feature_2: float = Field(..., description='Feature numeric 2')
    feature_3: float = Field(..., description='Feature numeric 3')


class PredictResponse(BaseModel):
    label: int
    probability: float | None = None
    model_version: str


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    model_version: str
