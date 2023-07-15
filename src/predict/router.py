from fastapi import APIRouter
from .schema import PredictRequest, PredictResponse
from .manager import PredictManager

router = APIRouter(prefix="/predict", tags=["predict"])

@router.get("/", response_model=PredictResponse, name="Make prediction")
async def predict(predict_request: PredictRequest):
    return await PredictManager.predict(predict_request)

